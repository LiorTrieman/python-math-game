# ----Example Python Program to create tables in disk file based SQLite databases----
# -- trying to save users in a table on the data base --
# -- importing the player module

# Import the sqlite3 module
import sqlite3
# Import sqlalchemy
from sqlalchemy import create_engine

# Create a database connection to a disk file based database
connectionObject = sqlite3.connect("Players.db")

# Obtain a cursor object
cursorObject = connectionObject.cursor()

# Create a  "players" table in the disk file based database - if not exist
sql_create_players_table = """ CREATE TABLE IF NOT EXISTS players (
                                    id integer PRIMARY KEY,
                                    player_name text NOT NULL,
                                    player_age integer,
                                    player_city text
                                ); """
# execute
cursorObject.execute(sql_create_players_table)
insertValues = "INSERT INTO players values(1, 'Lior', 'Tel-Aviv', 33)"
cursorObject.execute(insertValues)

insertValues = "INSERT INTO players values(2, 'Meron', 'Tel-Aviv', 6)"
cursorObject.execute(insertValues)

sql_create_scores_table = """CREATE TABLE IF NOT EXISTS scores (
                                id integer PRIMARY KEY,
                                player_id integer,
                                player_name text NOT NULL,
                                player_score integer,
                                score_date integer NOT NULL,
                                FOREIGN KEY (player_id) REFERENCES players (id)
                            );"""
cursorObject.execute(sql_create_scores_table)

insertValues = "INSERT INTO scores values(1, 1, 'Lior', 100, '2019-07-17')"
cursorObject.execute(insertValues)

insertValues = "INSERT INTO scores values(2, 1,'Meron', 99,'2019-07-17')"
cursorObject.execute(insertValues)


# Select from the players table
queryTable = "SELECT * from players"
queryResults = cursorObject.execute(queryTable)

# Print the players details:

# print("(Players in list:)")

for result in queryResults:
    pass
    #    print(result)


'''
database = "C:\sqlite\Players.db"
connectionObject = sqlite3.connect(database)
cursorObject = connectionObject.cursor()'''


connectionObject.close()

# Create an engine that connects to the census.sqlite file: engine
'''Absolute path # Windows
engine = create_engine('sqlite:///C:\\path\\to\\foo.db')'''

engine = create_engine("sqlite:///C:\\Users\\liort\\PycharmProjects\\MathGame\\DB\\Players.db")

# Print table names
print("list of tables in db:", engine.table_names())
