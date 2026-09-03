import re

# + Used matches 1 or more occurrence of preceding expression.
# \w  ==>  Match a single character : [A-Za-z0-9_]
name = ' MSC TECHNOLOGIES'
mo = re.search('\w+', name)
print(mo.group())


# * Used matches 0 or more occurrence of preceding expression.
name = '9148102585_MSC TECHNOLOGIES'
mo = re.search('\w*', name)
print(mo.group())

# \d  ==>  Match a digit   : [0-9]
name = '9148102585_MSC TECHNOLOGIES'
mo = re.search('\d*', name)
print(mo.group())

# '\'   ==> Used to remove special character functionality
name = 'MSC*123'
mo = re.search('MSC\*123', name)
print(mo.group())