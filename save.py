import json
 

def save_file(obj):

    with open("users.json", "w") as f:
        json.dump(obj, f)