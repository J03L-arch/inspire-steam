#Joel Mwega
#12/02/2026
#String formatting

#Get string length
sentence="Leave the football before the football leaves you"
sentence_length = len(sentence)
print(f"The length of sentence is: {sentence_length}")

#splitting a string
sentence_2 = "Games gone"
split = sentence_2.split(" ")

print(f"the first word is:",split[1])

#Make everything CAPS
mpesa_code = "ub2iddff2g"
capitalized = mpesa_code.upper()

print("New mpesa_code: ", capitalized)
small_letters=mpesa_code.lower()
print("New mpesa_code: ",small_letters)

#replacing characters in a string
balance= "180kes"
ammount_added="50kes"

cleaned_balance= balance.replace("kes","")
print("Cleaned balance :", cleaned_balance)
cleaned_ammount_added = ammount_added.replace("kes","")
print(f"Cleaned ammount added:{cleaned_ammount_added}")

new_balance= int(cleaned_balance) + int(cleaned_ammount_added)
print(f"New balance is {new_balance}")





