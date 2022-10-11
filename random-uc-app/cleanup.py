from api import api_call_dic
import requests

def clean_result(dic):
    
    res = requests.get('http://jsonplaceholder.typicode.com/users')
    result_obj = res.json()
    new_dct = {
        "id":result_obj[dic]['id'],
        "name":result_obj[dic]['name'],
        "username":result_obj[dic]['username'],
        "email":result_obj[dic]['email'],
    }
    print(new_dct)
    
    return new_dct