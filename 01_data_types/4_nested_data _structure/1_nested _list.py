'''
                                        MSC TECHNOLOGIES
                                 Job Oriented Training with Real Time
                    Mobile: 9148102585, 8121203075         msctechnologies111@gmail.com

'''

'''
1. A "nested list" means having lists inside another list
2. It helps to group similar types of data together
3. You can access each category or specific item using indexes
'''

# Example: list of fruits, vegetables, and dry fruits
items = [
    ['apple', 'banana', 'mango'],          # Fruits
    ['carrot', 'tomato', 'potato'],        # Vegetables
    ['almond', 'walnut', 'dates']          # Dry fruits
]

# Accessing full groups
print("Fruits list:",     items[0])
print("Vegetables list:", items[1])
print("Dry fruits list:", items[2])

# Accessing specific items
print("First fruit:",      items[0][0])
print("Second vegetable:", items[1][1])
print("Third dry fruit:",  items[2][2])

# PLEASE PRACTICE BELOW EXAMPLE 
d = [11,22,['A','B','C'],33,44,['A1','B2',[111,222,333]]]
