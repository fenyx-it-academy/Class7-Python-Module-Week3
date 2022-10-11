
import requests
import json


def save_file(obj,id):
	
	
	with open(f"User {id} .json", "w") as f:
		json.dump(obj, f)


def make_api_call():

	"""make api call and get the user information
	return: List - user info
	"""
	res = requests.get('http://jsonplaceholder.typicode.com/users')
	result_obj = res.json()
	return result_obj

def clean_result(dct,id_number):
	"""clean up a result obj 
	return: dict - cleaned up version of the res obj.
	"""
	
	
	new_dct = {
		"User_id": dct[id_number-1]['id'],
		"Name": dct[id_number-1]['name'],
		"Username": dct[id_number-1]['username'],
		"Email": dct[id_number-1]['email']	
	}
	return new_dct

def user_id():
	"""a function to get random user

	Returns:
		int: user's choice of user id
	"""
	print("Welcome to Userinfo App!")
	
	try:
		user_id_number=int(input('"Please provide the input id you want the learn information: " (between 1 and 10)'))
		assert 1<= user_id_number<=10
	
	except ValueError:
			print('Ooops that is not a valid input please try again...')
	except AssertionError:
			print("Please Enter a number between 1 and 10")

	return user_id_number