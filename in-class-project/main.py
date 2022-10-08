from get_currency import get_currency
from api import make_api_call
from cleanup import clean_result
from save_to_file import save_file




curr = get_currency()
result_dct = make_api_call(currency=curr)
clean_dct = clean_result(dct=result_dct)
save_file(obj=clean_dct)
