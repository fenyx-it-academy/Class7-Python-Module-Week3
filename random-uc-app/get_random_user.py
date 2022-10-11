def get_rdm_user():
    while True:
        print("\n Welcome to Random User Creator App! ")
        print ('\n This app generates random users from a database   ʕ•ᴥ•ʔ  \n')
        try:             
            user = int(input(" Please type how many random users you want to know: "))
            break
    
        except:
            print("\n   (;¬_¬)   Wrong choice...   (;¬_¬)  ")
    return user 