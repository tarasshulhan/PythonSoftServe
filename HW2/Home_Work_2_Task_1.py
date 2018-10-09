'''
Taras Shulhan
Python Core 355
Homework 2 Task 1
'''


import this
import codecs # for deciphering
from collections import Counter # to count words

# rotate the contents of this.s by 13 letters and save to variable
zen = codecs.encode(this.s, 'rot13')

zenList = zen.split() # split the string into a list of words
wordCount = Counter(zenList) # initialize counter with a list object
betterCount = wordCount['better'] # count how many times better is used and save to variable
neverCount = wordCount['never'] # count how many times never is used and save to variable
isCount = wordCount['is'] # count how many times is is used and save to variable

upperZen = zen.upper() # convert the string to all uppercase letters

amperZen = zen.replace('i', '&') # replace all i characters with ampersand

print('\n' + ('*'*35)+'\n"Better" was used {} times'.format(betterCount) +
      '\n"Never" was used {} times'.format(neverCount) +
      '\n"Is" was used {} times'.format(isCount) + '\n' + ('*'*35))

print("\nThe Zen of Python in all uppercase:\n\n" + upperZen + '\n' + ('*'*35))

print('\nThe Zen of Python with all "i" characters replaced by "&":\n\n' + amperZen)