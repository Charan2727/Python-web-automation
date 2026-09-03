'''
1. We can use all data types in for loop except number.
'''

## string iterate character by characters
s = 'MSC TECHNOLOGIES'
for c in s:
    print(c)

## LIST iterate value by value 
names = ['raja','mahi','kumar','nagesh', 'balu']
for name in names:
   print(name)

## TUPLE iterate value by value 
names = ('raja','mahi','kumar','nagesh', 'balu')
for name in names:
   print(name)

## SET iterate value by value 
names = {'raja','mahi','kumar','nagesh', 'balu'}
for name in names:
   print(name)

# Dictionary iterate based on key
emp_det = {'name':'MSC TECHNOLOGIES', 'mobile':9148102585, 'dname':'IT'}
for k in emp_det:
    print(k)

## Number object does not support for iterable
NO =  345
for n in NO: 
    print(n)
