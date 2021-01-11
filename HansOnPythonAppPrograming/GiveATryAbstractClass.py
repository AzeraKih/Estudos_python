##Define a abstract class `Animal` with an abstract method `say`.
##    Hint : Use 'abc' module
##Define a child class `Dog` derived from `Animal`.
##Also define a method 'say' which prints the message `I speak Booooo`.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def say(self):
        pass

class Dog(Animal):

    def say(self):
        return('I speak Booooo')

d = Dog()
d.say()

