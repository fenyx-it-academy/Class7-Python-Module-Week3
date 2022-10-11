import sys
import requests

def make_api_call():
    """make api call and get 10 user`s information
    return dictionary of list contain user`s information
    """    
    try:
        r = requests.get('http://jsonplaceholder.typicode.com/users')

    except Exception as e:
        print('Opps!', e, 'occured')
        sys.exit()

    else:
        result_obj = r.json()
        return result_obj