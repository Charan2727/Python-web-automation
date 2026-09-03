'''
1. Match is used to find a patran from starting positon
'''
import re

name = 'MSC TECHNOLOGIES'

mo = re.match('MSC', name)
print(mo.group())


