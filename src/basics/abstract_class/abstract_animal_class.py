from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

if __name__ == "__main__":
    dog = Dog()
    print(dog.make_sound())    

    