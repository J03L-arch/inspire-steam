#Name:Joel Mwega
#Date:16,02,2026
#Program: Defining functions

def cook_egg():
    oil="20ml"
    pan=True
    moto=True
    eggs= 2

    print(f"The pan is {pan} and the fire is {moto}, add {oil} of oil and cook {eggs} eggs")

print("Here is statement 1")
print("Here is statement 1")

cook_egg()

#Ride fares creating functions
def create_fare(route, distance, is_rush_hour):
    fare= distance*10
    if is_rush_hour== True:
        fare=fare *1.5

    print(f"Your fare to {route} is {fare}")
    return fare


returned_fare= create_fare("Juja-Allsops", 7, True)
print(f"The fare returned is {returned_fare}")

#Passing a list as a parameter
def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest} on sumn nonchalant king of the jungle shii")

all_interests=["Gooning", "Eating puh", "BJs", "cracking megalicious buns"]

write_all_interests(all_interests)



