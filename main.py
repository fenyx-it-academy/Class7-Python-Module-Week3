from utils import api_call, clean_result, saved, user_id

user_id_no = user_id()
result_list = api_call()

clean_dct = clean_result(dic=result_list,id_no=user_id_no)

saved(obj=clean_dct,id=user_id_no)