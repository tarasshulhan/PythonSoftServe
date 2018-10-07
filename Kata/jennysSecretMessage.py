"""
Taras Shulhan
Python Core Lv355
Kata: Jennys Secret Message
"""
def greet(name):
    if name == "Johnny": # check if the person is Johnny right away
        return "Hello, my love!"
    else: # add else
        return "Hello, {name}!".format(name=name) # only use this greeting if not johnny