import json
import sys
import requests
from datetime import datetime

def make_api_call():
   """make api call and get the information of the users
      return : list - user info
   """
   try:
      res = requests.get('http://jsonplaceholder.typicode.com/users')
      if res.status_code >= 400:
         raise requests.exceptions.HTTPError("There is an API error")

   except requests.exceptions.HTTPError as exc:
      print(exc)
      sys.exit()
   else:
      result_obj = res.json()
      return result_obj
   

def clean_up(lst):
   """clean up the result obj
      return: list - cleaned up version of the res obj
   """
   new_dict = dict()
   for item in lst:
    new_dict[item["id"]]=  {'name': item["name"], #"id" is the key of the new_dict
                    'username' : item["username"], 
                    'email' : item["email"]}

   return new_dict

def save_file(obj):
   """creates a file and saves the users data
   """
   filename = "result_" + datetime.now().strftime('%Y%m%d-%H%M%S')+'.json'
   with open(filename, "w") as f:
      json.dump(obj, f)