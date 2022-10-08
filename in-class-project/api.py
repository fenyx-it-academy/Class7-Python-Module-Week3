import sys
import requests


def make_api_call(currency):

    """make api call and get the latest conversion rate
    return: dict - currency info
    """

    try:
        res = requests.get(f'https://v6.exchangerate-api.com/v6/daa01c089871655d0660d4c8/latest/{currency}')
        if res.status_code >= 400:
            raise requests.exceptions.HTTPError("Unsupported currency, please make sure to type your currency correctly.")

    except requests.exceptions.HTTPError as exc:
        print(exc)
        sys.exit()
        
    else:
        result_obj = res.json()
        return result_obj
    
