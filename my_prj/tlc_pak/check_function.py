# -*- coding: utf-8 -*-
import re
from tlc_pak import detect_function as df, pars_patterns as pp
import io


def check_all_player(filename: str) -> str:
    output = ''
    in_game_id = 255
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(pp.for_game_id, line):
                in_game_id = df.game_id_detect(line, in_game_id)
            elif re.search(pp.spawn, line):
                output += df.player_spavn(line)
            elif re.search(pp.connect_start, line):
                output += df.player_nikname_detect(line)
            elif re.search(pp.death, line):
                output += df.death_detect(line)
            elif re.search(pp.command_de, line):
                output += df.command_detect(line)
            elif re.search(pp.g_chat, line):
                output += df.g_message_detect(line)
            elif re.search(pp.p_chat, line):
                output += df.p_message_detect(line)
            elif re.search(pp.logout, line):
                output += df.player_logout_detect(line)
    return output


def check_all_death(filename: str) -> str:
    output = ''
    in_game_id = 255
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(pp.for_game_id, line):
                in_game_id = df.game_id_detect(line, in_game_id)
            elif re.search(pp.spawn, line):
                df.player_spavn(line)
            elif re.search(pp.connect_start, line):
                df.player_nikname_detect(line)
            elif re.search(pp.death, line):
                output += df.death_detect(line)
    return output


def check_global_chat(filename: str) -> str:
    output = ''
    in_game_id = 255
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(pp.for_game_id, line):
                in_game_id = df.game_id_detect(line, in_game_id)
            elif re.search(pp.spawn, line):
                df.player_spavn(line)
            elif re.search(pp.connect_start, line):
                df.player_nikname_detect(line)
            elif re.search(pp.g_chat, line):
                output += df.g_message_detect(line)
    return output


def check_all_chat(filename: str) -> str:
    output = ''
    in_game_id = 255
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(pp.for_game_id, line):
                in_game_id = df.game_id_detect(line, in_game_id)
            elif re.search(pp.spawn, line):
                df.player_spavn(line)
            elif re.search(pp.connect_start, line):
                df.player_nikname_detect(line)
            elif re.search(pp.g_chat, line):
                output += df.g_message_detect(line)
            elif re.search(pp.p_chat, line):
                output += df.p_message_detect(line)
    return output


def look_for_him(a: str, steamid: str) -> str:
    if re.search(steamid, a):
        return a
    else:
        return 'None'


def check_with_steam_id(filename: str, steamid: str) -> str:
    output = ''
    in_game_id = 255
    with io.open(filename, 'r', encoding='utf-8') as log:
        for line in log:
            if re.search(pp.for_game_id, line):
                in_game_id = df.game_id_detect(line, in_game_id)
            elif re.search(pp.spawn, line):
                df.player_spavn(line)
            elif re.search(pp.connect_start, line):
                otvet = look_for_him(df.player_nikname_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(pp.death, line):
                otvet = look_for_him(df.death_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(pp.command_de, line):
                otvet = look_for_him(df.command_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(pp.g_chat, line):
                otvet = look_for_him(df.g_message_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(pp.p_chat, line):
                otvet = look_for_him(df.p_message_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
            elif re.search(pp.logout, line):
                otvet = look_for_him(df.player_logout_detect(line), steamid)
                if otvet != 'None':
                    output += otvet
    return output
