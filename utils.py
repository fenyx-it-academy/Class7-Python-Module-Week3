import json
from re import M
import requests 


def make_api(link):
    try : 
        r=requests.get(link)
        assert r.status_code  >=200 and r.status_code <=300
    except: 
      print('Error')  
    else:
        return r.json() 


def cleaning(dic):
    """ This would return a new dict , each key is an id for a user, each value for this key is another dict that contains
    other details, (id, name, user, email)
    """
    cleaned = {}
    for i in range(len(dic)) : 
        cleaned [str(i+1)]={}
        cleaned [str(i+1)]['id']=i+1
        cleaned [str(i+1)] ['name']=dic[i]['name']
        cleaned [str(i+1)] ['username']=dic[i]['username']
        cleaned [str(i+1)] ['email']=dic[i]['email']

    return cleaned 

def to_json(dic):
    with open('json_file.json', 'w') as j :
        json.dump(dic, j)
    


 