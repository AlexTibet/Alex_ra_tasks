# -*- coding: utf-8 -*-

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