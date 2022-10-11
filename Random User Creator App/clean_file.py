

def cleaning_json_file(result_object):
    """cleaning json file
        """
    new_lst = []
    for i in range (0,10):
            new_lst.append(result_object[i]["id"])
            new_lst.append(result_object[i]["name"])
            new_lst.append(result_object[i]["username"])
            new_lst.append(result_object[i]["email"])
    return new_lst

                