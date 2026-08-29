# Solved the condition
# ATM Withdrawal

# Ask user:
# Enter account balance:
# Enter withdrawal amount

# Rules:
# first condition 
# If withdrawal amount is greater than balance:
# Insufficient balance
# Otherwise calculate remaining balance

# second condition 
# If remaining balance is below 1000
# throw warning: low balance
# otherwise: transaction successful

# ye ju code hai mujhe isme elif use krna hoga, logical operator se kam nh hoga

# accountBalance = int(input("Enter your account balance: "));
# withDrawalAmount = int(input("Enter your with drawal amount: "));

# if withDrawalAmount > accountBalance:
#     print("Insufficient balance");
# elif accountBalance - withDrawalAmount < 1000:
#     print("You have withdrawn Rs.", withDrawalAmount);
#     print("Low balance")
# else:
#     print("You have with drawn Rs.", withDrawalAmount);

# A cinema has some rules:
# customer must be 18 or older
# if they are 18+, they must have a valid ticket, they have a valid ticket, they can enter 

# customerAge = int(input("Enter your age here: "));
# ticket = input("Do you have a ticket: ");

# if customerAge >= 18 and ticket == "yes":
#     print("Yeah im 18 plus", customerAge);
# else:
#     print("Entry are not allowed");

# isii question me aik aur condition. ab isme nested if use hogi, elif se kam nh hoga
# customerAge = int(input("Enter your age here: "));
# if customerAge >= 18: 
#     ticket = input("Do you have a ticket? ")
#     if ticket == "yes":
#         print("Entry allowed");
#     else:
#         print("You buy a ticket first")
# else:
#     print("Are you underage");

# ask userage, if they are under 18:
# you can not apply for a driving license
# if user is 18 or older, ask whether they passed
# driving test, if yes:
# license can be issued
# otherwise
# you need to pass the test

# userAge = int(input("Enter your age here: "))
# if userAge >= 18:
#     test = input("Driving test passed? ")
#     if test == "passed":
#         print("Are you eligible")
#     else:
#         print("You need to pass the test")    
# else:
#     print("you can not apply for a driving license");

# one more condition
# a university student can enroll in a course if
# they have completed the prerequisite course
# and their fees is paid

# student = input("You have completed the prerequisite course? ");
# if student == "complete":
#     fees = input("Your fees is paid? ")
#     if fees == "paid":
#         print("Are you eligible")
#     else:
#         print("first you can pay the fees");
# else:
#     print("first you can complete the prerequisite course");

# Ask passenger age.
# if age is 18 or above, ask whether they have a valid passport? 

# age = int(input("Enter your age: "))
# if age >= 18:
#     passport = input("Do you have a passport");
# if passport == "yes":
#     ticket = input("Do you have a ticket? ")
#     if ticket ==  "yes":
#         luggage = input("Do you have ecxess luggage? ")
#         if luggage == "yes":
#             print("Are you eligible")
#         else:
#     print("You dont have a ticket")
#     else:
#     print("Passport requiured")
   
# else:
#     print("Are you under 18")    
# not solved too many conditions in it!!
# solved again...