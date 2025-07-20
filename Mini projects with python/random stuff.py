k = 0
j = range(1, 201)
for i in j:
    k+=i
print (k)

def sum_n(n):
#Return the sum of the first n natural numbers using recursion.
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)
# Test the recursive sum against the formula: n(n+1)/2
for i in range(1, 11):
    recursive_sum = sum_n(i)
    formula_sum = i * (i + 1) // 2
    print(f"n = {i}: Recursive Sum = {recursive_sum}, Formula Sum = {formula_sum}")


# Define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Set operations in action
union_set = A.union(B) # Alternatively: A | B
intersection_set = A.intersection(B) # Alternatively: A & B
difference_set = A.difference(B) # Alternatively: A - B

print("Set A:", A)
print("Set B:", B)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (A - B):", difference_set)

import itertools
elements = ['a', 'b', 'c']
# All permutations of the list:
permutations = list(itertools.permutations(elements))
print("Permutations of ['a', 'b', 'c']:", permutations)

# All combinations of 2 elements:
combinations = list(itertools.combinations(elements, 2))
print("Combinations of 2 from ['a', 'b', 'c']:", combinations)