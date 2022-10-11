import json


def save_file(obj):

    with open('random-uc-app/ramdom_user_.json', "w") as f:
        json.dump(obj, f, indent=4)
