'''
Created on 24 mar 2018
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
Simple Example Inline With a List:
where %s is substitution from list
>>> print '%s %s %s'%('python','is','fun')
python is fun

'''
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

'Write a Python program to display the second and the third and fourth colors from the following list with commas'
color_list = ["Red","Green","White" ,"Black"]
print( "%s, %s, %s"%(color_list[1],color_list[2],color_list[3]))