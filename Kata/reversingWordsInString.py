"""
Taras Shulhan
Python Core Lv355
Kata: Reversing Words in a String
"""
def reverse(st):
    wordList = st.split((" ")) # split the string on whitespaces and save each word to a list while keeping whitespaces
    st = ' '.join(reversed(wordList)) # reverse the list and join it into a string adding a whitespace after each element
    return st # return the reversed string