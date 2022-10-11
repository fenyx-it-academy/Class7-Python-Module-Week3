import sys
import json
import requests
from datetime import datetime


  

def api_func():
    try:
        res = requests.get("http://jsonplaceholder.typicode.com/users")
         
    except Exception as x:
        print("Something went wrong...")
        sys.exit()

    else:
        result_object = res.json()
        return result_object




def clean_result(lst):

    new_list = []

    for i in range (0,10):
        new_list.append(lst[i]["id"])
        new_list.append(lst[i]["name"])
        new_list.append(lst[i]["username"])
        new_list.append(lst[i]["email"])
    return new_list


def create_file(new_list):

    dt_string = datetime.now().strftime("%d%m%Y%H%M%S")

    with open(f"users_{dt_string}.json", "w") as f:
        json.dump(new_list, f)