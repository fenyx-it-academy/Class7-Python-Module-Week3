from utils import api_func, clean_result, create_file

results = api_func()
clean_result = clean_result(results)
create_file(clean_result)