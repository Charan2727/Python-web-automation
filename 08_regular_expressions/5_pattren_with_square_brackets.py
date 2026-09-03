'''
1. Using square brackets "[]" Matches any single character in
'''
import re

# To match s is capital or samll letter in in [] position
name = 'Msctechnologies'
mo = re.match('[Mm]sctechnologies', name)
print(mo.group())

# To match "a to z" any small letter in [] position
mo = re.match('[a-z]sctechnologies', name)
print(mo.group())

# To match "A to E" any capital letter in [] position
mo = re.match('[A-E]sctechnologies', name)
print(mo.group())

# To match any one character in "akd43$." in [] position
mo = re.match('msc[akd43$.]', 'msc$')
print(mo.group())

# To match any one character a to z , A to Z, 0-9 in [] position
mo = re.match('M[a-zA-Z0-9]C', 'MSC')
print(mo.group())

# To match any one character except a to z in [] position
# if you use caret(^) symbol inside [] it will match anything except given charecters
mo = re.match('M[^a-z]C', 'MSC')
print(mo.group())

# To match any one character except r and a in [] position
mo = re.match('M[ra]C', 'MSC')
print(mo.group())
