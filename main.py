from utils import clean_result, make_api_call, create_file

result_lst = make_api_call()
clean_lst = clean_result(result_lst)
create_file(clean_lst)
