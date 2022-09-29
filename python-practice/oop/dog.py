class Dog:
    '''
    A simple class to define the properties of a dog
    '''
    species = 'Canis familiaris' # class attribute

    def __init__(self, name, age):
        '''
        Initialize the state of the class. These variables 
        are instance attributes because they only apply to the 
        single instance of the class. 
        '''
        self.name = name
        self.age = age

    def __str__(self):
        '''
        This function is referred to as an instance method
        because it can only be called from the class. Naming this
        function __str__ makes it a dunder method (because
        of the double underscore). This function gets called
        by print(variable of class instance),
        e.g.: max = Dog('Max', 4), print(max)
        '''
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    '''
    A child class that inherits from the Dog class. 
    child classes can overwrite information from the 
    parent class
    '''
    def speak(self, sound='Arf'):
        '''
        the super() calls the parent class's method 
        inside the child class
        '''
        return super().speak(sound)

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super.speak(sound)
