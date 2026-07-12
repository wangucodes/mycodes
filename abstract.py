from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    def display(self):
        print(f"name : {self.name} | Habitat {self.habitat}")
@abstractmethod
def speak(self):
    pass
class dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(habitat, name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} ({self.breed}) says: woof woof!")
class parrot(Animal):
    def __init__(self, habitat, name, phrase):
        super().__init__(self, habitat)
        self.phrase = phrase
    def speak(self):
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")
class lion(Animal):
    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride
    def speak(self):
        print(f"{self.name} (pride: {self.pride}) says:roaaar")
dog = Dog("bruno", "home", "labrador")
lion = Lion("simba", "savannah", "pride rock")
parrot = Parrot("polly", "jungle", "sqawk")
print("===Animal sound show===\n")
for animal in [dog, lion, parrot]
animal.display()
animal.speak()
print()