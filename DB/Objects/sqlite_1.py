
import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
  #  try:
    conn = sqlite3.connect(db_file)
    return conn
#    except Error as e:
 #       print(e)

 #   return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    c.execute(create_table_sql)


def main():
    database = "C:\sqlite\sqlite_py.db"

    sql_create_players_table = """ CREATE TABLE IF NOT EXISTS players (
                                        id integer PRIMARY KEY,
                                        player_name text NOT NULL,
                                        player_age integer,
                                        player_city text
                                    ); """

    sql_create_scores_table = """CREATE TABLE IF NOT EXISTS scores (
                                    id integer PRIMARY KEY,
                                    player_id integer,
                                    player_name text NOT NULL,
                                    player_score integer,
                                    score_date integer NOT NULL,
                                    FOREIGN KEY (player_id) REFERENCES players (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_players_table)
        # create tasks table
        create_table(conn, sql_create_scores_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()




