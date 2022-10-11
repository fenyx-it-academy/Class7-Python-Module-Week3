import json





def save_to_file(obj):
    with open ("result.json","w") as f:
        json.dump(obj, f)

