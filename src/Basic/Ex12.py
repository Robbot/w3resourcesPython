'''
Created on 26 mar 2018
Write a Python program to print the calendar of a given month and year.
@author: Roju
'''
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))