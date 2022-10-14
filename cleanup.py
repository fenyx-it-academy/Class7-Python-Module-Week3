def clean_result(result_lst):
    """clean up the result obj - takes a list returns a dic
    return: dict - cleaned up version of the res obj.    """
    global i 
    i=1
    result_dict = {} 
 
    for item in result_lst:   
        result_dict[f'PERSON{i}'] = {}
        result_dict[f'PERSON{i}']['id'] =item["id"]
        result_dict[f'PERSON{i}']['name'] = item["name"]
        result_dict[f'PERSON{i}']['username'] = item["username"]
        result_dict[f'PERSON{i}']['email'] = item["email"]
        i=i+1
    return result_dict
