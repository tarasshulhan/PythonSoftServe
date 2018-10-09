'''
Taras Shulhan
Python Core Lv 355
Kata Will There Be Enough Space?
'''


def enough(cap, on, wait):
    return 0 if cap >= on + wait else (on + wait) - cap