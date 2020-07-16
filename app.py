from database import get_entries, add_entry, create_table

menu = """Select section:
1) Add new entry
2) View entries
3) Exit

Your selection: """


def add_entry_to_database():
    new_entry = input("input new entry: ")
    date_of_new_entry = input("input date of new entry: ")
    add_entry(new_entry, date_of_new_entry)


def show_entries(entries):
    for entry in entries:
        print("entry: {0}\ndata:{1}\n\n".format(entry['content'], entry['date']))

create_table()

while (user_input := input(menu)) != "3":  # new python3.8 feature :=
    if user_input == "1":
        add_entry_to_database()
    elif user_input == "2":
        show_entries(get_entries())
    elif user_input == "3":
        print("exit")
    else:
        print("There are no such options")
