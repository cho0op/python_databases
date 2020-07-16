entries = []


def add_entry(entry, date):
    entries.append({"content": entry, "date": date})


def get_entries():
    return entries
