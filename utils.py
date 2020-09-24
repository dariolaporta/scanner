import json


def get_translations():
    _strings = open('strings.json')
    data = json.load(_strings)
    _strings.close()
    return data
