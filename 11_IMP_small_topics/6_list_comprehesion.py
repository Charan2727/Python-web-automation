'''
List comprehensions are used for creating new list from another iterables.

As list comprehension we can perform loop operations inside square brackets with conditions.
'''

l = [1, 2, 3, 4]
## Basic list comprehension to do addition of 10 fro each value in list and it will return all results in another list 
r = [ n + 10 for n in l]
print(r)

## list comprehension with if condition
r = [n + 2 for n in l if n > 2]
print(r)

## list comprehension with if and else condition
r = [n * 2 if n > 2 else n + 10 for n in l]
print(r)

