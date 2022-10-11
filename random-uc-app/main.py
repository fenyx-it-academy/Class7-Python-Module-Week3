from api import api_call_dic
from save_to_file import save_file
from utils import start


ram_user = start(0)
result_dct = api_call_dic(user= ram_user)
save_file(obj = ram_user)