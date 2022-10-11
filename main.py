from api import make_api_call
from cleanup import clean_result
from save_to_file import save_file

list_of_dict = make_api_call() 
clean_dict = clean_result(list_of_dict)
save_file (clean_dict, 'myfirstresult')
