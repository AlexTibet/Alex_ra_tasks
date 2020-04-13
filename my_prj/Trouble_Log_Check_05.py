import io
import re
import datetime
from PySide2.QtWidgets import *
from test_tlc_gui import Ui_MainWindow
import sys

# Create application
app = QApplication()

# Create form and init UI
Form = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()


# Hook Logic
output = 'Сначала выбери файл)'
file_name = ''


in_game_id = 255
in_game_id_bucket = {}
player_info = {}    # key = steamID, value = [in_game_id, ]
spawn_history = {}


def pb_ok_with_stid():
    global in_game_id
    in_game_id = 255
    steam_id = ui.lineEdit_SteamID.text()
    if len(steam_id) < 5:
        ui.textEdit.clear()
        ui.textEdit.insertPlainText('Нужно ввести SteamID')
    else:
        ui.textEdit.clear()
        try:
            ui.textEdit.insertPlainText(check_with_steam_id(file_name, steam_id))
        except FileNotFoundError:
            ui.textEdit.insertPlainText('Файл не выбран')


def pb_find_log_file():
    global file_name
    file_name = QFileDialog.getOpenFileName()[0]
    print(file_name)
    ui.lineEdit_for_log_file.setText(file_name)


def pb_check_death():
    global in_game_id
    in_game_id = 255
    ui.textEdit.clear()
    try:
        ui.textEdit.insertPlainText(check_all_death(file_name))
    except FileNotFoundError:
        ui.textEdit.insertPlainText('Файл не выбран')


def pb_check_global_chat():
    global in_game_id
    in_game_id = 255
    ui.textEdit.clear()
    try:
        ui.textEdit.insertPlainText(check_global_chat(file_name))
    except FileNotFoundError:
        ui.textEdit.insertPlainText('Файл не выбран')


def pb_check_all_chat():
    global in_game_id
    in_game_id = 255
    ui.textEdit.clear()
    try:
        ui.textEdit.insertPlainText(check_all_chat(file_name))
    except FileNotFoundError:
        ui.textEdit.insertPlainText('Файл не выбран')


def pb_check_all():
    global in_game_id
    in_game_id = 255
    ui.textEdit.clear()
    try:
        ui.textEdit.insertPlainText(check_all_player(file_name))
    except FileNotFoundError:
        ui.textEdit.insertPlainText('Файл не выбран')


ui.toolButton_forlog_file.clicked.connect(pb_find_log_file)
ui.Button_with_chek_SteamId.clicked.connect(pb_ok_with_stid)
ui.pushButton_for_all_death.clicked.connect(pb_check_death)
ui.pushButton_for_global_chat.clicked.connect(pb_check_global_chat)
ui.pushButton_all_chat.clicked.connect(pb_check_all_chat)
ui.pushButton_all_lpg.clicked.connect(pb_check_all)

# ************************************ ПАТТЕРНЫ *********************************************************************
connect_pattern = r'LogOnline: STEAM: Adding P2P connection information with user'
connect_start = r'LogBeastsOfBermuda: Display: Starting post login process for player'
# connect_stop = r'and spawned their character. Sending server rules and map data to user'
spawn = r'LogBeastsOfBermuda: Display: Respawning saved character with:'
for_game_id = r'BBGameModeBase::ReclaimAbandonedPawn - Searching for abandoned pawns for player ID'
death, death_name, death_id = r'PLAYER DEATH::Reason:', r'Dead Player Name:', r'Dead Player ID:'
death_dino, death_grow = r'Dead Player Creature:', r'Dead Player Growth:'
killer, kiiller_id = r'Killing Player Name:', r'Killing Player ID'              # после Killing Player ID нет пробела
killer_dino, killer_grow = r'Killing Player Creature:', r'Killing Player Growth:'
command_de, command_start, command_finish = r'LogUserCommands: Display: <PLAYER:', r'CMD:', r'>'
g_chat, p_chat, msg = r'Received Global Msg - From:', r'Private Dispatched Msg - From:', r'\] \|\| Msg:'
logout = r'LogOnline: STEAM: Closing channel 28500 with user '
# *******************************************************************************************************************


def time_detect(a: str):    # Определяет время только в стандартных строках, на начальных строках выдаст ошибку
    time = a[1:20].split('-')
    # year, month, day = time[0].split('.')
    hour, minutes, sec = time[1].split(':')[0].split('.')
    time = datetime.time(hour_detect(hour), int(minutes), int(sec))
    # date = datetime.date(int(year), int(month), int(day))
    return '\nМСК-' + str(time) + ' | '


def game_id_detect(a):
    global in_game_id
    in_game_id += 1
    in_game_id_bucket[str(in_game_id)] = [a[re.search(for_game_id, a).end():].strip()]
    player_info[a[re.search(for_game_id, a).end():].strip()] = [str(in_game_id)]


def player_spavn(a):
    last_spawn = a[re.search(spawn, a).end():]
    nik_spawn = last_spawn.split('for player')[-1].strip()
    char_spawn = last_spawn.split('for player')[0].strip()
    spawn_history[nik_spawn] = char_spawn
    return '{}{} | спавнится на дино ростом {}'.format(time_detect(a), nik_spawn, char_spawn.split(',')[0].split()[1])


def player_nikname_detect(a):
    nik_and_id = a[re.search(connect_start, a).end():].strip().split('with ID')
    player_info[nik_and_id[1].strip()] += [nik_and_id[0].strip()]
    gameid = player_info[nik_and_id[1].strip()][0]
    return '{}{}| В игре! | SteamID:{} c игровым ID:{}\n'.format(time_detect(a), nik_and_id[0], nik_and_id[1], gameid)


def player_logout_detect(a):
    st_id = a[re.search(logout, a).end():].strip()
    try:
        ing_id, nik = player_info[st_id][0], player_info[st_id][1]
    except (KeyError, IndexError):
        ing_id, nik = 'Неизвестно', 'Неизвестно'
    return f'{time_detect(a)}ID:{ing_id}| {nik} | Вышел из игры. | SteamID: {st_id}\n'


def death_detect(a):
    d_reson = a[re.search(death, a).end():(re.search(death_name, a).start()-2)].strip()
    d_name = a[re.search(death_name, a).end():(re.search(death_id, a).start()-2)].strip()
    d_id = a[re.search(death_id, a).end():(re.search(death_dino, a).start()-2)].strip()
    try:
        d_ing_id = player_info[d_id][0]
    except KeyError:
        d_ing_id = "КОСЯК"
        return '\n'
    d_dino = a[re.search(death_dino, a).end():(re.search(death_grow, a).start()-2)].strip()
    if d_reson == 'Respawned':
        d_grow = a[re.search(death_grow, a).end():(re.search(killer, a).start() - 2)].strip()[0:5]
        return '{}{} | РЕСПАВНИТ {} на росте {} | SteamID: {}, ИгровойID: {}\n'.format(
                                                                time_detect(a), d_name, d_dino, d_grow, d_id, d_ing_id)
    elif d_reson == 'Died from Extreme Stress':
        d_grow = a[re.search(death_grow, a).end():(re.search(killer, a).start() - 2)].strip()[0:5]
        return '{}{} | УМИРАЕТ от экстримального стресса на {} с ростом {} | SteamID: {}, ИгровойID: {}\n'.format(
                                                                time_detect(a), d_name, d_dino, d_grow, d_id, d_ing_id)
    elif d_reson == 'Took a Lethal Fall':
        d_grow = a[re.search(death_grow, a).end():].strip()[0:5]
        return '{}{} | УМИРАЕТ от  на {} с ростом {} | SteamID: {}, ИгровойID: {}\n'.format(
                                                                time_detect(a), d_name, d_dino, d_grow, d_id, d_ing_id)
    elif d_reson == 'Died from Lightning Strike':
        d_grow = a[re.search(death_grow, a).end():].strip()[0:5]
        return '{}{} | УМИРАЕТ от удара молнии на {} с ростом {} | SteamID: {}, ИгровойID: {}\n'.format(
                                                                time_detect(a), d_name, d_dino, d_grow, d_id, d_ing_id)
    else:
        d_grow = a[re.search(death_grow, a).end():(re.search(killer, a).start() - 2)].strip()[0:5]
        k_ = a[re.search(killer, a).end():(re.search(kiiller_id, a).start() - 2)].strip()
        k_id = a[re.search(kiiller_id, a).end():(re.search(killer_dino, a).start() - 2)].strip()
        k_ing_id = player_info[k_id][0]
        k_d = a[re.search(killer_dino, a).end():(re.search(killer_grow, a).start() - 2)].strip()
        k_g = a[re.search(killer_grow, a).end():].strip()[0:5]
        return '{}{} |{}| на своём {} {} УБИВАЕТ --> | {} |{}| на {} {}\n\t  |{}| УБИВАЕТ --> |{}|\n'.format(
                                time_detect(a), k_, k_ing_id, k_d, k_g, d_name, d_ing_id, d_dino, d_grow, k_id, d_id)


def search_id(nik):
    for i in player_info.keys():
        try:
            if player_info[i][1] == nik:
                return i
            else:
                continue
        except IndexError:
            continue

def command_detect(a):
    c_nik = a[re.search(command_de, a).end():re.search(command_start, a).start()].strip()
    c_body = a[re.search(command_start, a).end():re.search(command_finish, a).start()].strip()
    st_id = search_id(c_nik)
    ing_id = player_info[st_id][0]
    return f'{time_detect(a)}ID:{ing_id}| {c_nik} | Консольная комманда --> {c_body}'


def g_message_detect(a):
    gm_id = a[re.search(g_chat, a).end():re.search(msg, a).start()].strip().split('[')[-1]
    gm_nik = player_info[gm_id][1]
    g_msg = a[re.search(msg, a).end():].strip()
    gm_ing_id = player_info[gm_id][0]
    return f'{time_detect(a)}ID:{gm_ing_id}| {gm_nik} | в Глобал Чат --> {g_msg}'


def p_message_detect(a):
    pm_id = a[re.search(p_chat, a).end():re.search(msg, a).start()].strip().split('[')[-1]
    pm_nik = player_info[pm_id][1]
    p_msg = a[re.search(msg, a).end():].strip()
    pm_ing_id = player_info[pm_id][0]
    return f'{time_detect(a)}ID:{pm_ing_id}| {pm_nik} | в ЛС или Групп Чат --> {p_msg}'


def look_for_him(a, steamid):
    if re.search(steamid, a):
        return a
    else:
        return 'None'


def check_all_player(filename):
    # global output
    output = ''
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(for_game_id, line):
                game_id_detect(line)
            elif re.search(spawn, line):
                output += player_spavn(line)
            elif re.search(connect_start, line):
                output += player_nikname_detect(line)
            elif re.search(death, line):
                output += death_detect(line)
            elif re.search(command_de, line):
                output += command_detect(line)
            elif re.search(g_chat, line):
                output += g_message_detect(line)
            elif re.search(p_chat, line):
                output += p_message_detect(line)
            elif re.search(logout, line):
                output += player_logout_detect(line)
    return output


def check_all_death(filename):
    # global output
    output = ''
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(for_game_id, line):
                game_id_detect(line)
            elif re.search(spawn, line):
                player_spavn(line)
            elif re.search(connect_start, line):
                player_nikname_detect(line)
            elif re.search(death, line):
                output += death_detect(line)
    return output


def check_global_chat(filename):
    # global output
    output = ''
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(for_game_id, line):
                game_id_detect(line)
            elif re.search(spawn, line):
                player_spavn(line)
            elif re.search(connect_start, line):
                player_nikname_detect(line)
            elif re.search(g_chat, line):
                output += g_message_detect(line)
    return output


def check_all_chat(filename):
    output = ''
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(for_game_id, line):
                game_id_detect(line)
            elif re.search(spawn, line):
                player_spavn(line)
            elif re.search(connect_start, line):
                player_nikname_detect(line)
            elif re.search(g_chat, line):
                output += g_message_detect(line)
            elif re.search(p_chat, line):
                output += p_message_detect(line)
    return output


def check_with_steam_id(filename, steamid):
    output = ''
    otvet = ''
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(for_game_id, line):
                game_id_detect(line)
            elif re.search(spawn, line):
                player_spavn(line)
            elif re.search(connect_start, line):
                otvet = look_for_him(player_nikname_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(death, line):
                otvet = look_for_him(death_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(command_de, line):
                otvet = look_for_him(command_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(g_chat, line):
                otvet = look_for_him(g_message_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(p_chat, line):
                otvet = look_for_him(p_message_detect(line), steamid)
                if otvet !='None':
                    output += otvet
            elif re.search(logout, line):
                otvet = look_for_him(player_logout_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
    return output


def hour_detect(a):     # перевод времени на мск, надо найти способ получше
    if int(a) + 3 > 23:
        if int(a) + 2 > 23:
            if int(a) + 1 > 23:
                a = 2
            else:
                a = 1
        else:
            a = 0
    else:
        a = int(a) + 3.
    return int(a)




# Run main loop
sys.exit(app.exec_())