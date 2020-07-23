import datetime
import database

menu = """Select option:
1) Add new movie
2) View upcoming movies
3) View all movies
4) Watch a movie
5) View watched movies
6) Exit.
Your selection: """

database.create_table()


def add_movie_to_database():
    title = input("title: ")
    date = input("date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title, timestamp)


def show_movies_from_database(header, movies):
    print(header, ":")
    for movie in movies:
        date = datetime.datetime.fromtimestamp(movie[1])
        human_date = date.strftime("%d-%m-%Y")
        print("title: {0}; date of release: {1} \n".format(movie[0], human_date))


def mark_movie_as_watched():
    title = input("Title of movie you watched:")
    database.watch_movie(title)


while (user_input := input(menu)) != "6":
    if user_input == "1":
        add_movie_to_database()
    elif user_input == "2":
        upcoming_movies = database.get_movies(True)
        show_movies_from_database("UPCOMING MOVIES", upcoming_movies)
    elif user_input == "3":
        all_movies = database.get_movies(False)
        show_movies_from_database("ALL MOVIES", all_movies)
    elif user_input == "4":
        mark_movie_as_watched()
    elif user_input == "5":
        watched_movies = database.get_watched_movies()
        show_movies_from_database("Watched movies", watched_movies)
    elif user_input == "6":
        pass
    else:
        print("Invalid input")
