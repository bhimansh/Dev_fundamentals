# """
# Intent:
# This is a creational desgin pattern, which provides the interface to create an object
# using the superclass, but allows subclasses to alter the type of the objects 
# that will be created.

# When to Use:
# -> You want to delegate the responsibility of instantiating objects to subclasses.
# -> You have a family of products that share a common interface.
# -> You want to follow the Open/Closed Principle — open for extension but closed for 
#     modification.

# Examplar Problem:
# BMW is a vehical provider having a range of ProductionEngines 
# like Bike-><500ccEngine, Bike->>500ccEngine, Cars->Petrol(Turbo), Cars->Desiel(TwinTurbo).
# Now, Lets say BMW wants to launch new product with "Electric" Engine.
# Great news, right? But how about the code? 
# At present, most of your code is coupled to the "ICE" class. 
# Adding "Electric" into the ProductionLine would require making changes to the entire codebase. 
# Moreover, if later you decide to add another type of Engines, you will probably need to 
# make all of these changes again.
# As a result, you will end up riddled with conditionals that switch the ProductionLine 
# behavior depending on the class of ProductionEngines objects.
#
# ------------------------
#  Identified Factory Pattern components:
#  -> Product (ProductionEngines)
#  -> ActualProduct(ICE, Electric)
#  -> Creator (BMW)
#  -> ActualCreator (BMWICE, BMWElectric) 
# ------------------------
#
# """

from abc import abstractmethod, ABC

class ProductionEngines(ABC):
    @abstractmethod
    def start():
        pass
class BMW(ABC):
    @abstractmethod
    def produce_engine():
        pass

class ICE(ProductionEngines):
    def start(self):
        return "Beast Awaken!"
    
class Electric(ProductionEngines):
    def start(self):
        return "Sorry for my existence"

class BMWICE(BMW):
    def produce_engine():
        return ICE()

class BMWElectric(BMW):
    def produce_engine():
        return Electric()

def get_bmw_engine(eng_type='Ice'):
    print(f'Starting the {eng_type} Engine')
    if eng_type == 'Electric':
        return BMWElectric.produce_engine()
    return BMWICE.produce_engine()

eng = get_bmw_engine()
print(eng.start())

eng = get_bmw_engine(eng_type='Electric')
print(eng.start())




# Another Simpler Example:- 
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class AnimalCreator(ABC):
#     @abstractmethod
#     def create_animal(self):
#         pass

# class DogCreator(AnimalCreator):
#     def create_animal(self):
#         return Dog()

# # Client-Code
# def create_anima():
#     return DogCreator().create_animal()

# print(create_anima().speak())
