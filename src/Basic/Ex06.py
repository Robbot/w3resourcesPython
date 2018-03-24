'''
Created on 24 mar 2018
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list 
and a tuple with those numbers

How to remove warnings from code?
Another option would be disabling that check altogether (for all variables) in 
PyDev > Editor > Code Analysis > Others > Redefinition of builtin symbols

@author: Roju
'''
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)