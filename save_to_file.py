import json

def save_file(obj, filename):

    with open (f"{filename}.json", "w") as f:
        json.dump(obj, f)