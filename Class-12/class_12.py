# today we learn strings method
# first letter of every word is capitalize, the method called is title()

# text = "python is easy"
# print(text.title())

# only first letter is capatilize of your string
# text = "python is easy"
# print(text.capitalize())

# strip method use, remove extra space in your string
# text = "      python is easy     "
# print(text.strip())

# rstrip method use, remove extra space right in your string
# text = "         python is easy           "
# print(text.rstrip())

# lstrip method use, remove extra space left in your string
# text = "         python is easy           "
# print(text.lstrip());

# isalpha() method ye batata hai ke apke string me sirf alphabet hai ya number bh agar number ho gay tww output is false, else true

# userName = "Hassan";
# print(userName.isalpha());

# agar isalpha use kiya hai method agar ap string ke center me space bh dete hen, tab bh output is false

# ask user for a name. check if the name is valid
# userName = input("Enter your name here: ");
# print(userName.isalpha());

# isdigit() method ap use kare gay tw wo check kare ga, ke is string me ju value hai wo number hai ya nh number hai tw return true warna false
# value = "12345"
# print(value.isdigit())

# value = "12.5"
# print(value.isdigit())  // this is false bcz number ke ilawa kuch acceptable nh hai is method me . ye bh count hoga

# username = "ahmed123"
# print(username.isalnum())

# username = "123ahmed"
# print(username.isalnum())

# isalnum dekhe ga kiya is string me number or alphabet dono hai tw true ai ga
# username = "ahmed-123"
# print(username.isalnum())

# ye sirf string me space ko dekhe ga and output is true, else false 
# text = " "
# print(text.isspace())

# islower() ke method se wo batai ga ke apke string ki value lowercase me hai ya nh
# name = "hassan"
# print(name.islower())

# isupper() ke method se wo batai ga ke apke string ki value uppercase me hai ya nh
# name = "HASSAN"
# print(name.isupper())

# istitle dekhe ga apne ju string me value di hai uske har word ka first letter capital hai tw true warna false
# name = "Python Programming is Easy"
# print(name.istitle())   # False

# name = "Python Programming Is Easy"
# print(name.istitle())     # True

# ask user for a password
# if password contains only letters print that
# if password contains only numbers print that
# if password contains both, print password accepted

# userPassword = input("Enter your password: ");

# if userPassword.isalpha():
#     print("You have entered only alphabets")
# elif userPassword.isdigit():
#     print("You have entered only letters")
# elif userPassword.isalnum():
#     print("Password Accepted")
# else:
#     print("Wrong Password")

# text = "Python is easy and Python is powerful"
# print(text.find("Python"))

# text = "Python is easy and Python is powerful"
# print(text.rfind("Python"))

# fileName = "student.final.report.pdf"
# position = fileName.rfind(".")
# print(position)

# extension = fileName[position+1:]  # agar me position ke sath +1 ka use kroga tw jis word ko mene find kiya tha upper . isko tw ye count nh karega isko! isliye +1
# print(extension)

# userEmail = "abc@gmail.com";
# print(userEmail.partition("@"))  # mene partition krwaya @ se tw mujhe output me teen alag alag string mile hen! "abc" "@" "gmail.com" 

# userName = "Hassan"
# age = 21
# ab me isko aik print me kis tarah show krwao without concatenation

# print(f"My name is {userName} and I'm {age} years old")
# print ke baad f lagana lazmi hai taake python ko pata chale ke string ko format kiya gaya hai

# num1 = 500
# num2 = 3
# print(f"total: {num1 * num2}")

# average = 10/3
# print(average)
# ab iske decimals ko control krna hai tw
# print(f"{average:.1f}")
# .1f likho ya .4f decimals ke baad jitne bh number chahiye apko waha wo number ap likh sakte hen

# salary = 2500000;
# print(salary)
# print(f"Salary: Rs. {salary:,}")

# startswith ka method ye karta hai ke string ki value us alphabet se start ho rai hai ju me poch raha ho, and asee hi endswith ka event hai

# fileName = "report_2026.pdf"
# print(fileName.startswith("report"))
# print(fileName.endswith("pdf"))

# ask user for employee ID
# Must start with "EMP"
# Remaining part must contain digits
# Total length must be 8 characters
# Sample employee ID: EMP12345

# employeeId = input("Enter your employee ID: ");

# if employeeId.startswith("EMP") and len(employeeId) == 8 and employeeId[3:].isdigit():
#     print("Valid ID")
# else:
#     print("InValid ID")