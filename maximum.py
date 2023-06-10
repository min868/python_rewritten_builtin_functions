# custom maximum function without using any builtin functions

def custom_maximum(data):
    if data == []:
        return None
    else:
      for i in data:
        if i>=data[0]:
                maximum_value =i
    return maximum_value
