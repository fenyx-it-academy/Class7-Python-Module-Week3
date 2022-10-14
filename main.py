
from operator import imod
import api_call
import cleanup
import save

result_lst = api_call.make_api_call()
clean_dct = cleanup.clean_result(result_lst)
save.save_file(clean_dct)

