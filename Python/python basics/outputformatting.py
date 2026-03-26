#Name:Joel Mwega
#Date:17,02,2026
#Program: To format the output
import math

name= "Joel Mwega"
weight= 58 #Weight in kgs
height= 174 #Height in cm
fav_team= "LFC"

#1.Formatting using f string (Method I)
print(f"My name is {name} and I wiegh {weight} in kgs")

#2.Formatting using f string(Method II)
msg= f"My name is {name} and I support {fav_team}"
print(msg)

#3.Using .format
print("My name is {0} and I am {1}cm tall".format (name,height))

#4.Using output specifiers (%s)
print("The value of pi ")