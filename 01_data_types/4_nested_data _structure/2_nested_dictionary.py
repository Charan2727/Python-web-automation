'''
1. A "nested dictionary" means having dictionaries inside another dictionary
2. It helps to organize data into key–value pairs for easy access
3. You can access each category or specific item using keys
'''

# Example: fruits, vegetables, and dry fruits
items = {
    "fruits": {
        "fruit1": "apple",
        "fruit2": "banana",
        "fruit3": "mango"
    },
    "vegetables": {
        "veg1": "carrot",
        "veg2": "tomato",
        "veg3": "potato"
    },
    "dry_fruits": {
        "dry1": "almond",
        "dry2": "walnut",
        "dry3": "dates"
    }
}

# Accessing full groups
print("Fruits dictionary:",     items["fruits"])
print("Vegetables dictionary:", items["vegetables"])
print("Dry fruits dictionary:", items["dry_fruits"])

# Accessing specific items
print("First fruit:",      items["fruits"]["fruit1"])
print("Second vegetable:", items["vegetables"]["veg2"])
print("Third dry fruit:",  items["dry_fruits"]["dry3"])

# PLEASE PRACTICE BELOW EXAMPLE 
d = {'dict1':{1:'A', 2:'B', 3:{'name':'MSC TECH', 'mobile':9148102585}}}

