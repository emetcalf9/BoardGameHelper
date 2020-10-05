import sqlite3

def create_history_table():
    database = sqlite3.connect("BoardGameHelper")
    cur = database.cursor()
    createTable = 'CREATE TABLE IF NOT EXISTS HISTORY(Game varchar(50), Winner varchar(50), Score int, Date text, FOREIGN KEY(Game) REFERENCES GAMES(Name),FOREIGN KEY(Winner) REFERENCES PLAYERS(Name))'
    cur.execute(createTable)
    database.commit()


def add_game_to_history(game, winner, score):
    database = sqlite3.connect("BoardGameHelper")
    cur = database.cursor()
    checkgame = cur.execute(f"SELECT Name FROM GAMES WHERE Name like '%{game}%'").fetchall()
    if len(checkgame) == 0:
        print("Game not found. Try again")
        return 1
    gamecorrected = checkgame[0][0]
    gameresults = f"INSERT INTO HISTORY(Game, Winner, Score, Date) VALUES ('{gamecorrected}','{winner}', {score}, datetime('now'))"
    cur.execute(gameresults)
    database.commit()

def get_last_games(count):
    database = sqlite3.connect("BoardGameHelper")
    cur = database.cursor()
    gamehistory = cur.execute(f"SELECT Game, Winner, Score, date(Date) FROM HISTORY ORDER BY Date desc LIMIT {count}").fetchall()
    print("Game, Winner, Score, Date")
    for game in gamehistory:
        print(f"{game[0]}, {game[1]}, {game[2]}, {game[3]}")