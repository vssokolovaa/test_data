import json

with open("../files/users.json", "r") as file:
    people = json.load(file)
    users = []
    for i in people:
        users.append({"name": i["name"],
                      "gender": i["gender"],
                      "address": i["address"],
                      "age": i["age"],
                      "books": []})
