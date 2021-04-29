'''
Created on 2 kwi 2018
Write a Python program to get a new string from a given string where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.
'''
stri = str(input("Input the string : "))
def new_string(stri):
    if len(stri) >= 2 and stri[:2] == "Is":
        return stri
    return "Is " + stri

print("The output is "+new_string(stri))