import sqlite3
import random


def create_default_list():
    bglist = sqlite3.connect("BGList")
    cur = bglist.cursor()
    createTable = 'CREATE TABLE IF NOT EXISTS BGL(Name varchar(50), MinPlay int, MaxPlay int, Difficulty int)'
    cur.execute(createTable)
    addGame = 'INSERT INTO BGL values("Ticket to Ride",2,6,2)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Catan",3,6,2)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Terraforming Mars",1,5,4)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Dixit",3,6,1)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Scythe",1,5,4)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Viticulture",1,6,3)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Legendary",1,4,2)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Lost Cities (Card)",2,2,2)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Lost Cities (Board)",2,4,2)'
    cur.execute(addGame)
    addGame = 'INSERT INTO BGL values("Forbidden Desert",2,5,3)'
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
    print("Your choices are: " + str(option_list))
    goagain = ''
    while goagain.upper() != 'N':
        if len(option_list) == 1:
            print("You're only choice is " + option_list[0])
            return 0
        choice = random.randint(0, len(option_list) - 1)
        print("You should play " + option_list[choice])
        print("Would you like a different suggestion?")
        goagain = input()
        if goagain.upper() == 'Y':
            print("What? Are my suggestions not good enough for you?")
            option_list.remove(option_list[choice])
        else:
            print('''I'm not sure what that means, but I'll take it as a "Yes"''')
    print("Ok, Goodbye!")

