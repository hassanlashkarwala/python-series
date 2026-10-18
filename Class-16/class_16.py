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

fruits = "Apple", "Mango", "Banana"
first, second, third = fruits

print(second)

# Packing	Unpacking
# Multiple values ko ek variable mein collect karna
# student = "Ali", 20, "Lahore"	
# One variable receives multiple values

# Unpacking
# Collection se values ko separate variables mein assign karna
# name, age, city = student
# Multiple variables receive individual values