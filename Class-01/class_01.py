age = 21;
# age is variable name, 25 is the value
# = is not used for equality
# = stores the RHS value oto the variable on LHS
# = is caleed assignment operator
print(age)

x = 10;
print(x)

score = 50;
print(score)
score = 80;
print(score)
score = 100;
print(score)

studentName = "Hassan";
studentAge = 21;
studentMarks = 85;
print(studentName)
print(studentAge)
print(studentMarks)

# variable naming rules in python: 4 rules!
# jab bh variable name rakhe wo name meaning full hona chahiye
# variable name can contain any letter, numbers, or underscore _
# variable name can not start with a number: 1st_name XX
# variable name can not contain space: means my name ase nh myName ase!! myName (camelCase) my_name (snake case)
# variable name can not be a python reserver keywords
# True
# False
# None
# print
# in
# if

#* =============================
#* Data Types
#* =============================
#! now we learn data types
#? four data types in python
# 1. Integer: int: any whole number 5, 17, -9
# 2. Float: float: decimal values -0.99, 1.414, 22.6702
# 3. String: str: text: Ali, Karachi: Use " " or ' '
# 4. Boolean: bool: True / False

price = 250.0;  #jese hi decimal agaya value me wo float tyep ban jai gi
print(price)

isDone = True;
print(isDone)

print(type(isDone))
print(type("10"))
print(type(price))

#*===============================
#* Arithemtic Operators
#*===============================

# + addition
# - subtraction
# * multiplication
# / division hamesha output float me dega

print(15 + 10)
print(15 - 10)
print(15 * 10)
print(15 / 10)

#? agar hum chahte hen ke division kare aur float me answer na ai tw humein do baar // lagana hoga

print(10 // 3)  # ab float me answer nh aiga integer me answer ai ga
print(10 / 3)   # ye decimal me values dega means float

#* % remainder, modulus, modulo operator
print(10 % 3)

#* exponent (power) **
# agar jese 2 ki power 4 hai tw answer 16 write in python
print(2 ** 4)

print(10 + 5 * 2)

# PEMDAS Paranthesis, Exponent, Multiplication, Division, Add, Subtraction
print((10 + 5) * 2)

# print(10 - 4 // 2 + 5)
print(10 - 4 / 2 + 5)