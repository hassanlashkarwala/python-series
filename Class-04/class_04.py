# ask user for a number and display even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "Even Number")
# else:
#     print(num, "Odd Number")

#ask user for two number and display the larger numbe, which number is greater than second
# num1 = int(input("Enter first number: "));
# num2 = int(input("Enter second number: "));
# if num1 > num2:
#     print("Number one is greater than number two");
# else:
#     print("Number two is greater than number one");
# ye ju humne code likha hai ye sirf batai ga ke dono me konsa number baraa hai agar dono number same hue tw phr? ab humein aik aur condition chahiye hogi isliye elif ka use hoga

# now use this code with add elif!
# num1 = int(input("Enter first number: "));
# num2 = int(input("Enter second number: "));
# if num1 > num2:
#     print("Number one is greater than number two");
# elif num1 == num2:
#     print("Boths are same");
# else:
#     print("Number two is greater than number one");
# elif: combination of else-if
# if/else is useful for two decisions
# if there are more than two outcomes, we use elif!

# ask user for a number and display negative os positive.
# num = int(input("Enter number: "));
# if num > 0:
#     print(num, "is positive number")
# elif num == 0:
#     print(num, "is not a valid number")
# else:
#     print(num, "is negative number")

# ask user for marks and print the grade.
# 90+ -> A
# 80-89 -> B
# 70-79 -> C
# 60-69 -> D
# Below 60 -> F

# marks = int(input("Enter your marks here: "));
# if marks >= 90:
#     print("Your grade is A");
# elif marks >= 80:
#     print("Your grade is B");
# elif marks >= 70:
#     print("Your grade is C");       
# elif marks >= 60:
#     print("Your grade is D");      
# else:
#     print("Are you fail"); 

# ask user for temperature and display the weather
# 40 or above -> Very Hot
# 30-39 -> Hot
# 20-29 -> Pleasant
# Below 20 -> Cold

# temp = int(input("Enter a temperature: "));

# if temp >= 40:
#     print("Very Hot");
# elif temp >= 30:
#     print("Hot");
# elif temp >= 20:
#     print("Pleasant");
# else:
#     print("Cold");

# =======================
# Logical operators!
# =======================
# and - or - not
# and operator me dono condition same honi chahiye!
# or operator me koi bh aik condition true ho jai tw output true hi mile ga!
# not operator jhoota operator hai sahi ko galat batai ga and galat ko sahi!

# use or Operator
# logicalOrOperator = 2 == 2 or 4 > 5;
# print(logicalOrOperator); 

# logicalOrOperator = 10 > 2 or 4 != 5;
# print(logicalOrOperator);

# use and operator
# logicalAndOperator = 2 == 2 and 7 > 10;
# print(logicalAndOperator);

# use not operator
# logicalNotOperator = not 5 > 4;
# print(logicalNotOperator)

# use or & and Operator
# mixedCondition  = 10 > 5 or 3 < 1 and 3 > 4;
# print(mixedCondition);

# secMixedCondition = not (5>10 or 3<=3) and True; 
# print(secMixedCondition);

# A student can enter a competition if their age is at least 16 and they have registered
# age = int(input("Enter your age: "));
# registered = input("Are you registered? (Y/N): ")

# if age >= 16 and (registered == "Y" or registered == "y"):
#     print("Are you allowed to enter competition!!");
# else:
#     print("Are you not allowed");    

# Simple login: if username is "admin" and password is 1234
# print login successful else print incorrect username/password

userName = input("Enter your name: ");
password = int(input("Enter your password: "));

if userName == "admin" and password == 1234:
    print("Login Successful!!");
else:
    print("Incorrect password or username");    