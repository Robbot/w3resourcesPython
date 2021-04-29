'''
Created on 30 mar 2018
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 
return double the absolute difference
'''
def main():
    number = int(input("Input the number : "))
    print("Chosen number is",number)
    if number > 17:
        difference = number - 17
        print("The number is greater than 17 and doubled difference is",2*difference)
    else:
        lower = 17 - number
        print("The number is lower than 17 and doubled difference is",2*lower)
    
    
main()
