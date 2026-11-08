# marks = [15, 25, 30, 45];
# def analyze_marks(marks):
#     total = 0
#     lowest = marks[0]
#     highest = marks[0]

#     for mark in marks:
#         total += mark
#         if mark > highest:
#             highest = mark
#         if mark < lowest:
#             lowest = mark
#     return lowest, highest, total;

# t, h, l = analyze_marks(marks)
# print(t)
# print(h)
# print(l)

# now we can learn Tupil

# aik variable me multiple values ko store kr sakte hen and this type is tupil
# packing, unpacking

# Unpacking ka matlab hai ek collection ke andar maujood multiple values ko alag-alag variables mein assign karna.
# Packing ka matlab hai multiple values ko ek single variable mein collect karna.

# student = "Hassan", 22, "Karachi"
# print(student)
# print(type(student))

# student = ("Hassan", 22, "Karachi")
# name, age, city = student;

# print(name)
# print(age)
# print(city)

# fruits = "Apple", "Mango", "Banana"
# first, second, third = fruits

# print(second)

# Packing
# Multiple values ko ek variable mein collect karna
# student = "Ali", 20, "Lahore"	
# One variable receives multiple values

# Unpacking
# Collection se values ko separate variables mein assign karna
# name, age, city = student
# Multiple variables receive individual values

# first, second, *others = [10, 20, 30, 50, 70]
# print(first)
# print(second)
# print(others)

# first, *middle, last = ["Hassan",20,30,40,50]
# print(middle)
# print(type(middle))
# print(last)
# print(type(last))
# print(first)
# print(type(first))
# variable ke sath * hai means uske aagey wali ju bh remaining values hen wo la kr de do
# and uski type phr list aii gi bcz aik se ziada values hen 

# name, age, *_ = ["Monica", 22, "Doctor"]

# print(age)
# print(type(age))
# print(_)

# *_, profession, country  = ["Monica", 22, "Doctor", "Pakistan"]

# print(_)
# print(profession)
# print(country)

# para or arguments only
# def simple(numbers):
#   return numbers
# print(simple(20))

# now this condition
# userName = input("Enter your name here")

# def myName():
#     print("Welcome", userName)
# myName()

# def add_three(a, b, c):
#     return a + b + c

# numbers = [20, 30, 50]

# print(add_three(*numbers))
# print(type(add_three(*numbers)))

# User default Parameters
# userCountry = input("Enter your country here: ")
# userCity = input("Enter your city here: ")
# def describe_city(city, country= "pakistan"):
#     return country, city 

# addInfo = describe_city("User Country: " + userCountry,"User City: " + userCity)
# print(addInfo)

# create a fn analyze_numbers
# return total, number of even numbers, odd numbers

# numbers = [10, 15, 22, 31, 40, 51]
# def analyze_number(numbers):
#     total = 0
#     even = 0
#     odd = 0
#     for loop in numbers:
#         total += loop
#         if loop % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return total, even, odd

# total, even, odd = analyze_number(numbers)
# print(total)
# print(even)
# print(odd)

# def calculate_area(length, width):
#   ''' Calculates and return the area of a rectangle'''
#   return length * width
# print(calculate_area(10,5))

# print(calculate_area.__doc__) 