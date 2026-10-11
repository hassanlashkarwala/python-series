# def analyzeMarks(marks):
#     total = 0
#     highest = marks[0]
#     lowest = marks[0]

#     for mark in marks:
#         total += mark

#         if mark > highest:
#             highest = mark

#         if mark < lowest:
#             lowest = mark
#     print("Total", total)      
#     print("Highest", highest)      
#     print("Lowest", lowest)

# marks = [ 300, 400, 530, 220, 190 ]
# analyzeMarks(marks)      

# def createProfile(name, age, city, course):
#     print(name)
#     print(age)
#     print(city)
#     print(course)

# positional arguments
# createProfile("Hassan", 21, "karachi", "Python Course");

# keyword arguments, isme humein sequence ka khayal nh rakhna hai but variable name dena hai
# createProfile(city = "Lahore", name = "Yaseen", age = 21, course = "AI&DS");

# def calculateResult(name, english, maths, science):
#     total = english + maths + science
#     percentage = total / 300 * 100
#     print("Student Name:", name)
#     print("Total Marks:", total)
#     print("Percentage:", percentage)

# calculateResult("Ali", 80, 70, 50)
# calculateResult("Ahmed", 80, 50, 90)

# def calculatePercentage(marks, totalMarks):
#     percentage = marks / totalMarks * 100
#     print(percentage)

# calculatePercentage(120, 200)

# now we learn return keyword

# def calculatePercentage(marks, totalMarks):
#       percentage = marks / totalMarks * 100
#       return percentage;

# result = calculatePercentage(280, 300)
# print(result)

# def calculatePercentage(marks, totalMarks):
#     return marks / totalMarks * 100

# percentage = calculatePercentage(220, 240)
# if percentage >= 90:
#     print("Distinction!")
# else:
#     print("No distinction!") 

# def testFunction():
#     print("First")
#     return
#     print("Second")

# testFunction()
# return keyword ke baad koi code run nh hoga

# def double(number):
#     return number * 2

# answer = double(5)
# print(answer)

# local variable vs global variable
# local variable wo hai, ju apke function me banai gay ho unka scope sirf local ho means function ke bahir wo accessible nh hai that's called local variable
# global variable ko ap code me kahi bh access kar sakte hen

# def change():
#     global a
#     a = 20
#     print(a)

# change()
# agar mujhe local variable ko global banana hai tw global keyword likh kr us variable ka name
# print(a)
# ab ye variable mujhe function ke bahir bh accessible hai bcz global keyword

# now we used default parametervalue taake agar koi argument pass na kare tw error na ai balke default value ju save hai wo mil jai gi
# def greet(name="Student"):
#     print("Hello", name)

# greet("Ali")
# greet()

# def calculateBill(price, tax=5):
#     taxAmount = price * tax / 100
#     total = price + taxAmount
#     return total

# print(calculateBill(1000))
# print(calculateBill(1000, 10))

def calculateTotal(price, qty):
    return price * qty

def calculateDiscount(amount):
    return amount * 0.10

def final_bill(price, qty):
  total = calculateTotal(price,qty)
  discount = calculateDiscount(total)
  return total - discount

print(final_bill(1200, 2))