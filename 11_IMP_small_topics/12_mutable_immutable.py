"""
                                         MSC TECHNOLOGIES
                                  Job Oriented Training with Real Time
                     Mobile: 9148102585, 8121203075         msctechnologies111@gmail.com


Mutable: 
    If you do any changes in mutable objects the memory address doesn’t change.
    Mutable objects are list, dictionary, set
Immutable: 
    If you do any changes in immutable objects the memory address will change.
    Mutable objects are number, string, tuple

    id(): is a built-in function in Python that returns the memory address of an object. 
"""

name = "Sriram"
print(f"\n Memory address of name before change: {id(name)}")
name = "Sriram Kumar"
print(f"\n Memory address of name after change : {id(name)}")

l = ["MSC TECHNOLOGIES", 9148102585, "PYTHON", "SELENIUM"]
print(f"\n Memory address of list before change: {id(l)}")
l.append("ROBOT FRAMEWORK")
print(f"\n Memory address of list after change : {id(l)}")
