import sqlite3
import random
from PlayerOps import *

def create_default_list():
    bglist = sqlite3.connect("BGList")
    cur = bglist.cursor()
    createTable = 'CREATE TABLE IF NOT EXISTS BGL(Name varchar(50), MinPlay int, MaxPlay int, Difficulty int)'
    cur.execute(createTable)
    addGame = '''INSERT INTO BGL values("Ticket to Ride",2,6,2),
    ("Catan",3,6,2),
    ("Terraforming Mars",1,5,4),
    ("Dixit",3,6,1),
    ("Scythe",1,5,4),
    ("Viticulture",1,6,3),
    ("Legendary",1,4,2),
    ("Lost Cities (Card)",2,2,2),
    ("Lost Cities (Board)",2,4,2),
    ("Forbidden Desert",2,5,3)
    '''
    cur.execute(addGame)
    bglist.commit()


def reset_list():
    bglist = sqlite3.connect("BGList")
    cur = bglist.cursor()
    cur.execute("DROP TABLE BGL")
    create_default_list()


def add_game(name, minPlay, maxPlay, difficulty):
    bglist = sqlite3.connect("BGList")
    cur = bglist.cursor()
    addGame = f"INSERT INTO BGL values('{name}',{minPlay},{maxPlay},{difficulty})"
    cur.execute(addGame)
    bglist.commit()


def remove_game(name):
    bglist = sqlite3.connect("BGList")
    cur = bglist.cursor()
    checkgame = cur.execute(f"Select NAME FROM BGL WHERE Name like '%{name}%'")
    id = checkgame.fetchall()
    if len(id) != 1:
        print("There was a problem with the name")
        return 1
    remove = f"DELETE FROM BGL WHERE Name ='{name}'"
    cur.execute(remove)
    bglist.commit()


def play_a_game():
    print("How many people are playing?")
    num_players = input()
    bglist = sqlite3.connect("BGList")
    cur = bglist.cursor()
    sqlquery = f'SELECT Name FROM BGL WHERE MinPlay <= {num_players} and MaxPlay >= {num_players}'
    cur.execute(sqlquery)
    options = cur.fetchall()
    option_list = []
    for option in options:
        option_list.append(option[0])
    if (len(option_list) == 0):
        print("There are no games that support that number of players")
        play_a_game()
        return 1
    print("Your choices are: " + str(option_list))
    goagain = ''
    while goagain.upper() != 'N':
        if len(option_list) == 1:
            print("You're only choice is " + option_list[0])
            return 0
        choice = random.randint(0, len(option_list) - 1)
        print("You should play " + option_list[choice])
        print("Would you like a different suggestion? (Y/N)")
        goagain = input()
        if goagain.upper() == 'Y':
            option_list.remove(option_list[choice])
        elif goagain.upper() == 'N':
            pickfp = input('Would you like help picking the first player?\n')
            if pickfp.upper() == 'Y':
                pick_first_player()
            break
        else:
            print('''I'm not sure what that means, but I'll take it as a "Yes"''')


def list_all_games():
    bglist = sqlite3.connect("BGList")
    cur = bglist.cursor()
    sqlquery = '''SELECT * FROM BGL'''
    cur.execute(sqlquery)
    games = cur.fetchall()
    print('Name, Minimum Players, Maximum Players, Difficulty')
    for game in games:
        print(f'{game[0]} {game[1]} {game[2]} {game[3]}')
    print()