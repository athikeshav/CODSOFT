#Password Generator
import random
import string
print("Password Generator")
length=int(input("enter the desired length of the password:"))
i=0
password=''
for i in range(length):
    password+=random.choice(string.ascii_letters)
    
print("password = ",password)