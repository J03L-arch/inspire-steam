#Name:Joel Mwega
#Date:13,02,2026
#Program: Program to calculate arithmmetic progressions

#calculating nth term

a= int(input("Enter the first term:"))
n= int(input("Enter the the number of terms:"))
d= int(input("Enter the common difference:"))
r=int(input("Enter the common ratio:"))

nth_term= int (a+ (n -1)*d)
print(f"The nth term is{nth_term}")
Sn= int(n/2 *((2*a + (n-1)*d)))
print (f"Sum of the terms is: {Sn}")
Sn=int((a*((r**n)-1))/(r-1))
