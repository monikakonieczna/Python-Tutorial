"""
Positional arguments
Keyword arguments
*args:
    contents: allows for unlimited variables to be passed into a function without defining them ahead of time
**kwargs
    contents: allows for unlimited keyword arguments to be passed into a function without defining them ahead of time
"""


def user_info(name, age=0, city="Tucson"):
    """This function prints name, age and city from an argument provided to the function.
    #argument #keyword_argument #*kwargs #*args"""

    print("{} is {} years old, from {}.".format(name, age, city))


user_info("Janet", 58, "Oklahoma City")
user_info("Michael")
