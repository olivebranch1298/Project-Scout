import json


def load_profile():
    with open("config/profile.json") as file:
        return json.load(file)