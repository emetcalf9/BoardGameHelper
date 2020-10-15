import random
import sqlite3


def create_player_table():
    database = sqlite3.connect("BoardGameHelper")
    cur = database.cursor()
    createTable = 'CREATE TABLE IF NOT EXISTS PLAYERS(Name varchar(50))'
    cur.execute(createTable)
    database.commit()


def check_player_name(name):
    database = sqlite3.connect("BoardGameHelper")
    cur = database.cursor()
    result = cur.execute(f"Select Name from PLAYERS where Name = '{name}'").fetchall()
    if len(result) == 1:
        return True
    else:
        return False


def pick_first_player(num_players):
    database = sqlite3.connect("BoardGameHelper")
    cur = database.cursor()
    player_list = []
    count = 1
    while count <= int(num_players):
        player = input(f"Player {count}'s name: ")
        player_list.append(player)
        count += 1
        # Check if player already exists in Players table and add if not exists
        if not check_player_name(player):
            cur.execute(f"INSERT INTO PLAYERS(Name) Values ('{player}')")
            database.commit()
    fplayernumber = random.randint(0, len(player_list)-1)
    print(f'{player_list[fplayernumber]} is the first player\n')
    input("Press enter to continue\n")
