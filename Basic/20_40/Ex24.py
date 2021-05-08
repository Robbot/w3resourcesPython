#24. Write a Python program to test whether a passed letter is a vowel or not.
# vowels = ["a", "e", "i", "o", "u"]
# user_letter = input("Please provide a letter and check is this vowel or not: ")
#
# for n in range(5):
#     if user_letter == vowels[n]:
#         print("It is vowel! ")
#         break
#     else:
#         print("It is not vowel! ")
#         break
#
#Or solution is like that:
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
user_letter = input("Please provide a letter and check is this vowel or not: ")
print(is_vowel(user_letter))

