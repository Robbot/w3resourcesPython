'''
Created on 4 kwi 2018
Write a Python program to count the number 4 in a given list
@author: Roju
'''
def main():
    def list_count_4(nums):
        count = 0
        for num in nums:
            if num == 4:
                count = count + 1
        return count
    print(list_count_4([1, 4, 6, 7, 4]))
    print(list_count_4([1, 4, 6, 4, 7, 4]))
    
if __name__ == "__main__":
    main()