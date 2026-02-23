#Name:Joel Mwega
#Date:23,02,2026
#Program: To show inheritance in python

class Animal():
    def __init__(self, species, weight, food):
        self.species= species
        self.weight= weight
        self.food= food

    def grow(self,weight):
        weight= 1.1* weight
        print(f"The animal weighs {weight} kgs")

    def eat(self, food):
        print(f"The animal eats {food}")
  
class Dog(Animal):
    def __init__(self, colour, height, breed):
        super(). __init__(species, weight, food)
        self.height= height
        self.breed= breed
        self.colour= colour

    def eat(self,bark):
        print(f"The dog says woof woof {bark}") 
    