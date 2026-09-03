'''
D/B SHALLOCOPY AND DEEP COPY?
SHALLOCOPY
    	Creates a new object, but nested objects are shared between the original and copied object. 
    	Faster than deep copy. 
    	Uses less memory. 
DEEP COPY
    	Creates a new object and copies all nested objects recursively. 
    	Original and copied objects are completely independent. 
    	Slower than shallow copy. 
    	Uses more memory. 
'''

import copy
names = ["Sriram", "Kumar", "MSC", "Technologies"]
original_list = [0, names, 3, 4]

# Shallow Copy
shallow = copy.copy(original_list)

# Deep Copy
deep = copy.deepcopy(original_list)

names.append("RRR")  # Changed

print(f"\n SHALLOW COPY CHANGES  : {shallow}")     # CHANGED
print(f"\n DEEP COPY NOT CHANGED : {deep}")        # NOT CHANGED 





print()