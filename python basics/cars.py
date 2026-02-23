#Name:Joel Mwega
#Date:23,02,2026
#Program: To show classes in python

class Car():
    #Attributes
    def __init__(self,model,make,colour,year):
        self.model= "Challenger"
        self.make= "Dodge"
        self.colour= "Matte Black"
        self.year= "2019"
    
    #print car details
    def print_details(self,model, make, colour, year):
        print(f"The {colour} {make} {model} was first manufactured in {year}.")

#instantiate a clas object
my_car= Car("Challenger", "Dodge", "Matte Black", "2019")
wifeys_car= ("RS7", "Audi", "White", "2018")

my_car.print_details("Challenger", "Dodge", "Matte Black", "2019")




