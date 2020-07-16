import sqlite3

entries = []

connection = sqlite3.connect('data.db')


def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")


def add_entry(entry, date):
    with connection:
        connection.execute("INSERT INTO entries VALUES (?,?);", (entry, date))


def get_entries():
    return entries
