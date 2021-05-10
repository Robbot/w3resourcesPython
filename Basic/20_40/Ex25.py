"""25. Write a Python program to check whether a specified value is contained in a group of values
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""


def is_in_list(num):
    numbers = [1, 5, 8, 3]
    return num in numbers


num = int(input("Please enter a number: "))
# print(f"See True if this number is in list of numbers or False if it is not: {is_in_list(num)}")
if is_in_list(num) == True:
    print(f"{num} is in the list of numbers")
else:
    print(f"{num} is not in the list of numbers")

"""Sample solution was
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
"""
