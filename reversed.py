# custom reverse function without using any builtin functions

def custom_reversed(lst):
    new_lst=[]
    for i in lst:
        new_lst=[i]+new_lst
    return new_lst
