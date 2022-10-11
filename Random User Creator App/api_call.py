import sys
import requests






def make_api_call():
    """
    make an api call.
    """
    try:
        r = requests.get("http://jsonplaceholder.typicode.com/users")
        if r.status_code >= 400:
            raise requests.exceptions.HTTPError("No internet connection")
    except requests.exceptions.HTTPError as e:
        print(e)
        sys.exit()
    else:
        result_object = r.json()
        return result_object
