import random

def get_names(a):
    try:
        list = [1, 2, 3,4,5,6,7,8,9]
        c = random.sample(list,int(a) )
        return c
    except Exception as e:
        return e; 