'''
🔹 Combination of Nested List and Dictionary
1. We can mix both — dictionary containing lists, or lists containing dictionaries
2. Useful for organizing grouped and labeled data
'''

l = [9148102585, 'MSC TECH', [11,22,['1A', '2B'],33], ('A', 'B', 'C'), {1: 'A', 2: 'B', 3:['X','Y','Z']}]


# TO PRINT 22
print(l[2])



# PLEASE PRACTICE SIMILAR EXAMPLE WITH LIST CONTAINING ALL DATA TYPES
items = {
    "fruits": ['apple', 'banana', 'mango'],
    "vegetables": ['carrot', 'tomato', 'potato'],
    "dry_fruits": ['almond', 'walnut', 'dates']
}

print("Fruits      :",    items["fruits"])

print("Second fruit:",    items["fruits"][1])


print("Third dry fruit:", items["dry_fruits"][2])