'''
Created on 4 kwi 2018
Write a Python program to find whether a given number (accept from the user) is even or odd, print out 
an appropriate message to the user
@author: Roju
'''
def main():
    x = int(input("Input the number : "))
    if x%2==0:
        print("The number is odd")
    else:
        print("The number is even")
        
if __name__ == "__main__":
    main()