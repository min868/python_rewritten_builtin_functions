# custom_absolute function without using any builtin functions

def custom_absolute(num):
    try:
        if float(num)<0:
            return -num
        else:
            return num
    except ValueError as err:
        print(err)    
        