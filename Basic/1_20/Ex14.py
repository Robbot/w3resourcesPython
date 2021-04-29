'''
Created on 26 mar 2018
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
from datetime import date
y = int(input("Input the year : "))
m = int(input("Input the month : "))
d1 = int(input("Input the first day: "))
d2 = int(input("Input the last day: "))
f_date = date(y, m, d1)
l_date = date(y, m, d2)
delta = l_date - f_date
print("The difference is "+str(delta.days)+" days")