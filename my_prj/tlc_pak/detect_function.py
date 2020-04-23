# -*- coding: utf-8 -*-
import datetime
import re
from tlc_pak import pars_patterns as pp

in_game_id_bucket = {}
in_game_id = 255
player_info = {}    # key = steamID, value = [in_game_id, ]
spawn_history = {}


def hour_detect(a: str) -> int:     # перевод времени на мск, надо найти способ получше
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


def time_detect(a: str) -> str:    # Определяет время только в стандартных строках, на начальных строках выдаст ошибку
    time = a[1:20].split('-')
    hour, minutes, sec = time[1].split(':')[0].split('.')
    time = datetime.time(hour_detect(hour), int(minutes), int(sec))
    return f'\nМСК-{str(time)} | '


def game_id_detect(a: str, in_game_id: int) -> int:
    in_game_id += 1
    in_game_id_bucket[str(in_game_id)] = [a[re.search(pp.for_game_id, a).end():].strip()]
    player_info[a[re.search(pp.for_game_id, a).end():].strip()] = [str(in_game_id)]
    return in_game_id


def player_spavn(a: str) -> str:
    last_spawn = a[re.search(pp.spawn, a).end():]
    nik_spawn = last_spawn.split('for player')[-1].strip()
    char_spawn = last_spawn.split('for player')[0].strip()
    spawn_history[nik_spawn] = char_spawn
    spawn_grow = char_spawn.split(',')[0].split()[1]
    return f'{time_detect(a)}{nik_spawn} | спавнится на дино ростом {spawn_grow}'


def player_nikname_detect(a: str) -> str:
    nik_and_id = a[re.search(pp.connect_start, a).end():].strip().split('with ID')
    player_info[nik_and_id[1].strip()] += [nik_and_id[0].strip()]
    gameid = player_info[nik_and_id[1].strip()][0]
    return f'{time_detect(a)}{nik_and_id[0]}| В игре! | SteamID:{nik_and_id[1]} c игровым ID:{gameid}\n'


def player_logout_detect(a: str) -> str:
    st_id = a[re.search(pp.logout, a).end():].strip()
    try:
        ing_id, nik = player_info[st_id][0], player_info[st_id][1]
    except (KeyError, IndexError):
        ing_id, nik = 'Неизвестно', 'Неизвестно'
    return f'{time_detect(a)}ID:{ing_id}| {nik} | Вышел из игры. | SteamID: {st_id}\n'


def death_detect(a: str) -> str:
    d_reson = a[re.search(pp.death, a).end():(re.search(pp.death_name, a).start()-2)].strip()
    d_name = a[re.search(pp.death_name, a).end():(re.search(pp.death_id, a).start()-2)].strip()
    d_id = a[re.search(pp.death_id, a).end():(re.search(pp.death_dino, a).start()-2)].strip()
    try:
        d_igid = player_info[d_id][0]
    except KeyError:
        return '\n'
    d_dino = a[re.search(pp.death_dino, a).end():(re.search(pp.death_grow, a).start()-2)].strip()
    if d_reson == 'Переродился':
        d_gr = a[re.search(pp.death_grow, a).end():(re.search(pp.killer, a).start() - 2)].strip()[0:5]
        return f'{time_detect(a)}{d_name} | РЕСПАВНИТ {d_dino} на росте {d_gr} | SteamID: {d_id}, ИгровойID: {d_igid}\n'
    elif d_reson == 'Вы умерли от сильного стресса':
        d_gr = a[re.search(pp.death_grow, a).end():(re.search(pp.killer, a).start() - 2)].strip()[0:5]
        return f'{time_detect(a)}{d_name} | УМИРАЕТ от экстримального стресса на {d_dino} с ростом {d_gr} ' \
               f'| SteamID: {d_id}, ИгровойID: {d_igid}\n'
    elif d_reson == 'Смертельное падение':
        d_gr = a[re.search(pp.death_grow, a).end():].strip()[0:5]
        return f'{time_detect(a)}{d_name} | УМИРАЕТ от смертельного падения на {d_dino} с ростом {d_gr}' \
               f' | SteamID: {d_id}, ИгровойID: {d_igid}\n'
    elif d_reson == 'Died from Lightning Strike':
        d_gr = a[re.search(pp.death_grow, a).end():].strip()[0:5]
        return f'{time_detect(a)}{d_name} | УМИРАЕТ от удара молнии на {d_dino} с ростом {d_gr} ' \
               f'| SteamID: {d_id}, ИгровойID: {d_igid}\n'
    else:
        try:
            d_gr = a[re.search(pp.death_grow, a).end():(re.search(pp.killer, a).start() - 2)].strip()[0:5]
        except AttributeError:
            return f'\n\n\n\n Что-то новенькое!\nскиньте мне файл и эту строку)\n{a}\n\n\n\n'
        k_ = a[re.search(pp.killer, a).end():(re.search(pp.kiiller_id, a).start() - 2)].strip()
        k_id = a[re.search(pp.kiiller_id, a).end():(re.search(pp.killer_dino, a).start() - 2)].strip()
        k_ing_id = player_info[k_id][0]
        k_d = a[re.search(pp.killer_dino, a).end():(re.search(pp.killer_grow, a).start() - 2)].strip()
        k_g = a[re.search(pp.killer_grow, a).end():].strip()[0:5]
        return f'{time_detect(a)}{k_} |{k_ing_id}| на своём {k_d} {k_g} УБИВАЕТ --> | {d_name} |{d_igid}| ' \
               f'на {d_dino} {d_gr}\n\t  |{k_id}| УБИВАЕТ --> |{d_id}|\n'


def search_id(nik: str) -> str:
    for i in player_info.keys():
        try:
            if player_info[i][1] == nik:
                return i
            else:
                continue
        except IndexError:
            continue


def command_detect(a: str) -> str:
    c_nik = a[re.search(pp.command_de, a).end():re.search(pp.command_start, a).start()].strip()
    c_body = a[re.search(pp.command_start, a).end():re.search(pp.command_finish, a).start()].strip()
    st_id = search_id(c_nik)
    try:
        ing_id = player_info[st_id][0]
    except KeyError:
        ing_id = f'\n\nКосяк, вот оригинальная сторока:\n{a}\nСкорее всего сделал что-то до того как ему' \
                 f' назначился айди\n\n'
    return f'{time_detect(a)}ID:{ing_id}, {st_id}| {c_nik} | Консольная комманда --> {c_body}'


def g_message_detect(a: str) -> str:
    gm_id = a[re.search(pp.g_chat, a).end():re.search(pp.msg, a).start()].strip().split('[')[-1]
    gm_nik = player_info[gm_id][1]
    g_msg = a[re.search(pp.msg, a).end():].strip()
    gm_ing_id = player_info[gm_id][0]
    return f'{time_detect(a)}ID:{gm_ing_id}, {gm_id}| {gm_nik} | в Глобал Чат --> {g_msg}'


def p_message_detect(a: str) -> str:
    pm_id = a[re.search(pp.p_chat, a).end():re.search(pp.msg, a).start()].strip().split('[')[-1]
    pm_nik = player_info[pm_id][1]
    p_msg = a[re.search(pp.msg, a).end():].strip()
    pm_ing_id = player_info[pm_id][0]
    return f'{time_detect(a)}ID:{pm_ing_id}, {pm_id}| {pm_nik} | в ЛС или Групп Чат --> {p_msg}'
