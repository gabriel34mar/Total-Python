"""Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type."""
def list_attributes(**kwargs):
    result=list(kwargs.values())
    return result
    