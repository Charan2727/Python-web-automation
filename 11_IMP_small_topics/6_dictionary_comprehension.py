'''
Python allows dictionary comprehensions. We can create dictionaries using simple expressions. 
A dictionary comprehension SYNTAX ==>  {key: value for (key, value) in iterable}

dictionary comprehensions we can perform loop operations inside Curly Braces with conditions.
'''


## Using dictionary comprehensions we can find each character  repeated count in a string
## Here each character  become key and that character  repeated count become value
s = 'hellow'
d = {c:s.count(c) for c in s}
print(d)

## dictionary comprehension with if condition to get only which character repeated more than one time
s = 'hellow'
d = {c:s.count(c) for c in s if s.count(c) > 1}
print(d)


