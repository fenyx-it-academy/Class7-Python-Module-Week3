import sys
import requests


def make_api_call():

    """make api call and get a list of random users. """

    try:
        result_response = requests.get('http://jsonplaceholder.typicode.com/users')
        # print("result type is ", type(result))
        if result_response.status_code >= 400:
            raise requests.exceptions.HTTPError("Un error is raised, status code above")

    except requests.exceptions.HTTPError as raisedException:
        print(raisedException)
        sys.exit()
        
    else:
        result_obj_lst = result_response.json()
        return result_obj_lst
    

    


