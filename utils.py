import requests
import json


def saved(obj,id):


	with open(f"User {id} .json", "w") as f:
		json.dump(obj, f)


def api_call():

	"""an api call and user info
	return: user info
	"""
	res = requests.get('http://jsonplaceholder.typicode.com/users')
	result_obj = res.json()
	return result_obj

def clean_result(dic,id_no):


	new_dic = {
		"UserID": dic[id_no-1]['id'],
		"Name": dic[id_no-1]['name'],
		"UserName": dic[id_no-1]['username'],
		"E-mail": dic[id_no-1]['email']	
	}
	return new_dic

def user_id():
	"""random user picker
	return: int: user id
	"""
	print("Welcome to the UserID App!")

	try:
		user_id_no=int(input('"Type a number between 1 and 10: '))
		assert 1<= user_id_no<=10

	except ValueError:
			print('Please enter a valid input')
	except AssertionError:
			print("Please Enter a number between 1 and 10")

	return user_id_no