def clean_result(list_of_dict):
    """clean up result obj
    return dict of celan up version of result obj 
    """    
    new_list = []
    for i in list_of_dict:
        l = {'id':i['id'], 'name': i['name'], 'username': i['username'], 'email': i['email']}
        new_list.append(l)
        
    new_dict = {item['id']:item for item in new_list}
    return new_dict 