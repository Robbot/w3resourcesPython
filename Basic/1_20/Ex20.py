'''
Created on 4 kwi 2018
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''

def larger_string(letters, n):
    result = ""
    for i in range(n):
        result = result + letters
    return result

letters = input("Provide letters to be repeated: ")
n = int(input("How many times should it repeated? "))

print(larger_string(letters, n))