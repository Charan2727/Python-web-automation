'''
  1. Logical operators are "and" , "or" , "not
  2. Using logical operations we can execute a block of code based on multiple condition.

  Both conditions are True (AND example)
  At least one condition is True (OR example)
  Condition is reversed (NOT example)

  # LOGICAL "AND" OPERATOR TABLE 
    A	B	A and B
    T	T	   T
    T	F	   F
    F	T	   F
    F	F	   F

  # LOGICAL "OR" OPERATOR TABLE
    A	B	A or B
    T	T	   T
    T	F	   T
    F	T	   T
    F	F	   F
'''

sal = 50
dname = 'SALES'

# AND operator example
if sal >= 500 and dname == 'IT':
    print('AND CONDITION TRUE → SAL IS ::', sal + 100)
else:
    print('AND CONDITION FALSE')

# OR operator example
if sal >= 500 or dname == 'IT':
    print('OR CONDITION TRUE → SAL IS ::', sal + 100)
else:
    print('OR CONDITION FALSE')

# NOT operator example
if not dname == 'IT':
    print('NOT CONDITION TRUE → DEPT IS NOT IT')
else:
    print('NOT CONDITION FALSE → DEPT IS IT')
