# now start comparison operators in python
# 1. greater than  >
# 2. less than <
# 3. greater than or equal to >= 
# 4. less than or equal to <=
# 5. equal to ==
# 6. not equal to !=

# int or string ko ap aps me compare nh krwa sakte hen python error through kr degi

# print(10 > 5)
# print(10 < 5)

# age = 20;
# print(age > 18)
# print(age > 25)

# is_raining = True
# is_holiday = False
# print(type(is_raining))
# print(type(is_holiday))

# a = 15;
# b = 10;
# print(a < b)
# print(a > b)
# print(a == b)
# print(a != b)

# marks = 50
# print(marks >= 40)
# print(marks <= 40)

# userAge = input("Enter your age: ");
# print(userAge > 18)
# yaha integer or string ko apas me compare nh krwa sakte hen hum dono alag alag data type hen input hamesha string return krta hai
# tw isliye input ko int me convert krna parega isliye input se phele int(input())

# Input -> variable -> comparison -> True/False

# userAge = int(input("Enter your age: "))
# print(userAge > 18)

# if it is raining, take an umbrella
# agar barish ho rahi hai tw umbrella le kar jao, means if

# raining = True;
# if raining:
#     print("Take an Umbrella!")
# ye print se phele ju gap araha hai isko khete hen indentation.

# age = 22
# if age > 18:
#     print("Are you Adult"); #agar condition true tw dono print run hogay
#     print("Thank you"); 
# print("Welcome") #ab me agar gap nh doga is print me gap nh diya tw, tw iska condition se ab koi taluq nh hai khudi print kare ga

# ask user for marks, if marks are 50 or more print Pass.

# userMarks = int(input("Enter marks: "));
# if userMarks >= 50:
#     print("Are you Pass");
#     print("Good boy")
# else:
#     print("Are you Fail");
#     print("Practice more")

# else isliye use kiya hai ke agar meri if condition false ho tw else ka use kro means else ki condition run hogi

# ask user for a number, print positive or negative
# userNumber = int(input("Enter a number: "));
# if userNumber > 0:
#     print("Positive");
# else:
#     print("Negative")

# ask for two number, display which one is greater than

a = int(input("Enter fist Number: "))
b = int(input("Enter second Number: "))

if a > b:
    print("A is greter than B");
else:
    print("B is greater than A")

# we learn in next class boths are same ? So how i used a condition
# rn only learn which value is greater than!

# Home Work
# ask user for a number, and use condition user value is even or odd?     