#Name:Joel Mwega
#Date:23,02,2026
#Program: To perform file operations

#Create new file
new_file= open("Student_data.txt", "r+")

#Write to new file
new_file.write("{Student name: Joel Mwega, ID: 12311, email: joelmwega12311@gmail.com}")
new_file.close()

#Read new file
new_file= open("Student_data.txt", "r+")
data= new_file.read()
print(data)
new_file.close()

#Delete file
#use os module
import os
os.remove("remove.txt")

#delete folder
os.rmdir("folder")
