import json


def load(path):
    out = None
    with open(path, "r") as f:
        out = json.load(f)
    return out


def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f)

