for r in range (10):
    print([r], end=" " )
for x in range(10,20,2):
    print(x,end=" ")

Total = 0
numbers = range(50)
for x in numbers:
    Total+=x
print("Total =", Total)


word = input('Enter a word ')
for w in word:
       print(f"Letter: {w}")

#to count the vowels in a word
trial = input('enter a word with a lot of vowels ').lower()
count = 0
for t in trial:
    if t in 'aeiou':
          count+= 1
print ('The number of vowels in this word is: ', {count})

#to get the first 10 multiples of a number
num = int(input("Enter a number "))
for n in range(1, 11):
    result = num * n
    print(f'{num} x {n} = {result}')

big = [3, 4, 5, 6, 10, 15, 4, 67, 4, 5, 56, 3]
biggest = big[0]
for b in big:
    if b > biggest:
        biggest = b
print(f'The biggest number in this list is, {biggest}')

#to print fruits and thier index using the enumerate function
fruits = ['apple', 'banana', 'cherry']
for index, f in enumerate(fruits, start = 1):
    print (f"word {index}: {f}")

    
#exercise 9, separating odd and even in separate lists
oddAndEven = [1, 3, 56, 90, 33, 77, 88, 67, 46, 31, 87, 44, 100, 111, 45]
odd = []
even = []
for num in oddAndEven:
    if num%2 == 0:
       even.append(num)
    else:
       odd.append(num)
       
print (f'even numbers ;{even}')
print (f'odd numbers; {odd}')

#exercise 10
word = input('enter a word ')
for i in range(len(word) - 1, -1, -1):
    print(word[i], end='')


#nexted loop
for i in range(1,6):
    for j in range (1,6):
        k = j*i
        print ("{:3d}".format(k), end=' ')
    print()

number = int(input('enter a number: '))
for w in range(1, number+1):
    for m in range(1, number+1):
        print('*', end=" ")
    print()

numeric = int(input('enter a number'))
count = 1

for row in range(numeric):
    for col in range(numeric):
        print(count, end="\t")  # tab space for neatness
        count += 1
    print()  # move to next line after each row


mains = ['rice', 'spaghetti', 'Yam', 'Indomie']
sides = ['beans', 'plantain', 'egg', 'boiled egg']
for m in mains:
    for s in sides:
        print("you can combine", m , "and",  s, end="\n")
    print()

#to print seat numbers
seat = ['A', 'B', 'C', 'D']
num = range(1, 4)
for s in seat:
    for n in num:
        print (f"{s}{n}", end= " ")
    print()
