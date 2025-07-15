zen = """
Beautiful is better than ugly./
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated
"""
for char in zen:
    if char not in "aeiou":
        print (char, end='')

numbers = [40, 50, 60, 33,77,65, 48, 29, 30, 19, 17,55, 46, 38, 90]
print('The even numbers in this list are: ', )
for num in numbers:
    if num %2 == 0:
        print(num, end = ',')

