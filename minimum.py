# custom minimum function without using any builtin functions

def custom_minimum(data):
    if data==[]:
        return None
    else:
        for i in data: 
            if i<=data[0]:
                minimum_value =i
        return minimum_value
