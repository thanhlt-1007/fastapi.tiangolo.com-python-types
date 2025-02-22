"""
Python Types Intro

Python has support for optional "type hints" (also called "type annotations").

These "type hints" or annotations are a special syntax that allow declaring the type of a variable.

By declaring types for your variables, editors and tools can give you better support.

This is just a quick tutorial / refresher about Python type hints.
It covers only the minimum necessary to use them with FastAPI... which is actually very little.

FastAPI is all based on these type hints, they give it many advantages and benefits.

But even if you never use FastAPI, you would benefit from learning a bit about them.
"""

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))

"""
The function does the following:

-   Takes a first_name and last_name.

-   Converts the first letter of each one to upper case with title().

-   Concatenates them with a space in the middle.
"""

"""
Edit it

It's a very simple program.

But now imagine that you were writing it from scratch.

At some point you would have started the definition of the function, you had the parameters ready...

But then you have to call "that method that converts the first letter to upper case".

Was it upper? Was it uppercase? first_uppercase? capitalize?

Then, you try with the old programmer's friend, editor autocompletion.

You type the first parameter of the function, first_name, then a dot (.) and then hit Ctrl + Space to trigger the completion.

But, sadly, you get nothing useful:
"""

"""
Add types

Let's modify a single line from the previous version.

We will change exactly this fragment, the parameters of the function, from:
    first_name, last_name

to
    first_name: str, last_name: str

That's it:

Those are the "type hints":

That is not the same as declaring default values like would be with:
    first_name="john", last_name="doe"

It's a different thing.

We are using colons(:), not equals(=).

And adding type hints normally doesn't change what happens from what would happen without them.

But now, imagine you are again in the middle of creating that function, but with type hints.

At the same point, you try to trigger the autocomplete with Ctrl + Space and you see:

With that, you can scroll, seeing the options, until you find the one that "rings a bell":
"""
