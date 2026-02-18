#Name:Joel Mwega
#Date:16,02,2026
#Program: To show lists in python

friends=["Rachel", "Phoebe", "Ross", "Chandler", "Monica", "Joey"]
print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("Jack")
print(friends)

new_friends= ["Joe", "Unc", "Kimberly", "Gentrix", "Bena"]
print(len(new_friends))

students= friends + new_friends
print(students)
students.insert(5,"Bombooo")
print(students)
students.insert(9,"Puh")
print(students)
students.extend("Joe")
print(students)
students.remove("Joey")
print(students)
 
new_students=students.copy()
print(new_students)
print(students.count("Joe"))
