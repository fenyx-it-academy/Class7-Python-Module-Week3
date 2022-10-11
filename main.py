from utils import make_api_call, clean_up, save_file

result_list = make_api_call()
clean_dict = clean_up(result_list)
save_file(clean_dict)
