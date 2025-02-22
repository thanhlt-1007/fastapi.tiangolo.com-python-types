def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old " + str(age)
    return name_with_age

"""
More motivation

Check this function, it already has type hints:

Because the editor knows the types of the variables, you don't only get completion, you also get error checks:

Now you know that you have to fix it, convert age to a string with str(age):
"""

"""
Declaring types

You can use, for example:

-   int

-   float

-   bool

-   bytes
"""
