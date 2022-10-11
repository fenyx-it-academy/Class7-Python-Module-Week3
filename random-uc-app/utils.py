from cleanup import clean_result
from get_random_user import get_rdm_user
import random


def rdm_num (rdm):
    rdm = random.choice(range(1,10))
    return rdm

def start (spu):
    spu = get_rdm_user()
    
    for vr in range(spu):
        dit = (clean_result((rdm_num(0))))
    return dit