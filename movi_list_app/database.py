import sqlite3, datetime

connection = sqlite3.connect('data.db')


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS movies (title TEXT, release_timestamp REAL, watched INTEGER)")



def add_movie(title, release_timestamp):
    with connection:
        connection.execute("INSERT INTO movies VALUES (?,?,0);", (title,
                                                                  release_timestamp))


def get_movies(upcoming=False):
    cursor = connection.cursor()
    if upcoming:
        today_timestamp = datetime.datetime.today().timestamp()
        cursor.execute("SELECT * FROM movies WHERE release_timestamp>?;", (today_timestamp,))
    else:
        cursor.execute("SELECT * FROM movies;")
    return cursor.fetchall()

def get_watched_movies(upcoming=False):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE watched=1")
    return cursor.fetchall()

def watch_movie(title):
    with connection:
        connection.execute("UPDATE movies SET watched=1 WHERE title=?", (title,))
