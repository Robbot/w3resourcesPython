'''
Created on 26 mar 2018
Write a Python program to get the volume of a sphere with radius 
V=4/3*pi*radius^3
'''
import math
def main():
    r = int(input("Input the radius of sphere : "))
    Volume=4/3*math.pi*(r*r*r)
    print ("The Volume of sphere is: "+str(Volume))
main()