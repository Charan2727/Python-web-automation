'''
1. Search is used to find a patran any where in the string 
'''
import re

name = '9148102585 MSC TECHNOLOGIES'
mo = re.search('MSC', name)
print(mo.group())



