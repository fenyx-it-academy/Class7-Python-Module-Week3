from utils import *

user_id_number = user_id()
result_list = make_api_call()

clean_dct = clean_result(dct=result_list,id_number=user_id_number)

save_file(obj=clean_dct,id=user_id_number)