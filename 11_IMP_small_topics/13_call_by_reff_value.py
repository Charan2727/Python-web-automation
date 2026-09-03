"""
Call by Reference: 
    Instead of copying the value, it copy the memory address of the original variable. so changes affect in both variable.

Call by Value:
    It copies the value of the original variable to new variable. so changes affect only in new variable.

NOTE:    Bydefault PYTHON is a call by refference language. But, if we want to make it call by value then we can use copy module in python.

"""


names = ["Sriram", "Kumar", "MSC", "Technologies"]
print(f"\n Memory address of names  : {id(names)}")
names_2 = names
print(f"\n Memory address of names_2: {id(names_2)}")
'''
NOTE : I have changed the names_2 list but it will reflect in names list also because both are referring to same memory address.
'''
names_2.append("RRR")
print(f"\n names   : {names}")
print(f"\n names_2 : {names_2}")


print()