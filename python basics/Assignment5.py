#Name:Joel Mwega
#Date:16,02,2026
#Program: To calculate  income tax of employee

salary=int(input("Enter your gross salary:"))
if salary< 50000:
    tax= (2.5 * salary)/100
    net_salary= salary- tax

print(f"Gross salary={salary}")    
print(f"tax={tax}")
print(f"net salary={net_salary}")