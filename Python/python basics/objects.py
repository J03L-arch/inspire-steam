#Name:Joel Mwega
#Date:19,02,2026
#Program: Defining an object

class Human:
    #First define the attributes
    type= "mammal"
    legs= 2
    brain= True
    warm_blooded= True
    city= "Nairobi"
    #We then create a constructor for the object/class
    #The constructor will be used to create copies of this object
    def __init__(self, name, age):
        self.human_name= name 
        self.human_age= age
    
    def tell_story(self):
        print(f"Hello, I am {self.human_name}. Here is my story")
        print("There once was an unemployed homeboy")

#Creating a Human
Jeff= Human("Jeff", 17)
Dwayne= Human("Dwayne",17)
print(Jeff.human_age)
print(17)

#Let the human created do things
Jeff.tell_story

#Modify the object's attributes
Jeff.city= "Kiambu"
print("Jeff's location:" ,Jeff.city)
print("Dwayne's location:", Dwayne.city)
