'''
Created on 2 kwi 2018
Write a Python program to calculate the sum of three given numbers, if the values are equal then return 
thrice of their sum. So, for unequal numbers just a sum, but for equal number return a sum multiplied by three.
'''
x = int(input("Input the number : "))
y = int(input("Input the number : "))
z = int(input("Input the number : "))

def sum_thrice(x, y, z):

    suma = x + y + z
  
    if x == y == z:
        suma = suma * 3
    return suma

print("The result is "+str(sum_thrice(x, y, z)))