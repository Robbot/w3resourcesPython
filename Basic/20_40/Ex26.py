#Write a Python program to create a histogram from a given list of integers.
rng = int(input("How many lines do you want to print "))
char = input("What kind of char do you want to duplicate: ")
items = []
n = 1
while n <= rng:
    item = int(input(f"Provide number of items in the line {n} "))
    items.append(item)
    n += 1
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += char
          times = times - 1
        print(output)

histogram(items)