import json
import sys
import requests
from datetime import datetime


def make_api_call():

    """make api call to get user information
    return: list - user info
    """

    try:
        res = requests.get('http://jsonplaceholder.typicode.com/users')
        if res.status_code >= 400:
            raise requests.exceptions.HTTPError("There is a connection error")

    except requests.exceptions.HTTPError as exc:
        print(exc)
        sys.exit()
        
    else:
        result_obj = res.json()
        return result_obj


############################################################################3


def clean_result(lst):
    """clean up a result obj 
    return: list- keeps only (id, name, username, email)
    """
    new_lst = []
    for i in range (0,10):
        new_lst.append(lst[i]["id"])
        new_lst.append(lst[i]["name"])
        new_lst.append(lst[i]["username"])
        new_lst.append(lst[i]["email"])

    return new_lst



    ##########################################################################

def create_file(new_lst):
    """creates a file with the users data
    """

    dt_string = datetime.now().strftime("%d%m%Y%H%M%S")

    with open(f"users_{dt_string}.json", "w") as f:
        json.dump(new_lst, f)