'''
POLYMORPHISM

If the same method name is used in different classes
but performs different actions, it is called Polymorphism.
'''

# Base Class
class Animal:
    def sound(self):
        print("Animal makes a sound.")

# Child Class
class Dog(Animal):
    def sound(self):
        print("Dog says: Bow Bow 🐶")

# Child Class
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow 🐱")

# Child Class
class Cow(Animal):
    def sound(self):
        print("Cow says: Mooo 🐮")


dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()