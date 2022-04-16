import json
from read_csv import books
from read_json import users

while len(books):
    for i in users:
        if len(books) > 0:
            i['books'].append(books.pop())

with open("data_file.json", "w") as f:
    s = json.dumps(users, indent=4)
    f.write(s)
