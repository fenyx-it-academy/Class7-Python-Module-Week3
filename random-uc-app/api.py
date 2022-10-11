import requests
import sys

def api_call_dic(user):
    
    res = requests.get('http://jsonplaceholder.typicode.com/users')
    result_obj = res.json()
    try:        
        (res.status_code) # code 200
        
        if res.status_code >= 400:
            raise requests.exceptions.HTTPError(" Sorry, the database is not available! ʕ •`ᴥ•´ʔ ")

    except requests.exceptions.HTTPError as exc:
        print(exc)
        sys.exit()
    
    return result_obj