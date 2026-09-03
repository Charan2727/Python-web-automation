'''
   What is abstract ?
   Abstraction is a process of hiding the implimentation details and only show important functionality.
1. For Abstract class we can't create an instance.
1. An abstract method is a method that is declared, but contains no implementation.
2. By defining an abstract base class, you can define a common API for a set of subclasses.
3. By using abc module we can define abstract class.
'''
from abc import ABCMeta,abstractmethod

class One(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        print(' One Add ')

    @abstractmethod
    def sub(self):
        pass

# We can't create an instance of abstract class
#a = One()
#a.add()

## If you inheritence an abstaruact class you should impliment that all those methods which are abstract ,methods
class Two(One):
    def add(self):
        print(' TWO ADD')

    def sub(self):
        pass

ins = Two()
ins.add()


