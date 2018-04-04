'''
Created on 4 kwi 2018
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
@author: Roju
'''

def larger_string(stri, n):
    result = ""
    for i in range(n):
        result = result + stri
    return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))