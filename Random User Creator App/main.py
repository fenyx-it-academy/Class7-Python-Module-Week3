from api_call import *
from clean_file import *
from save_file import *
import sys
import requests






raw_list = make_api_call()
clean_file = cleaning_json_file(raw_list)
save_file = save_to_file(clean_file)




 






