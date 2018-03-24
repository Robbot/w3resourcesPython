'''
Created on 20 mar 2018
Write a Python program to display the current date and time.
@author: Roju
'''
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))