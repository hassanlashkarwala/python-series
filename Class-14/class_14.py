# marks = 450
# totalMarks = 500
# percentage = marks / totalMarks * 100
# print(percentage)

# what if we 500 students, we will face code duplication
# Functions: A function is a named set of instructions
# that we can use whenever we need it
# Input -> percentage calculator -> Output

# def calculatePercentage():      # function define
#     marks = 450;
#     totalMarks = 500;
#     percentage = marks / totalMarks * 100;
#     print(percentage);

# calculatePercentage();    # function calling

# def sayHello():
#     print("Hello");
#     print("start programming");

# sayHello();

# def greet():
#   print('Welcome to Python')

#def keyword used to define a function
# greet function name
# ( ) parantheses used in the definition and call
#  indented code: instructions exectude when called

# greet()
# greet()
# greet()
# greet()
# greet()
# i call the function five times

# def first():
#   print('First')
# def second():
#   print('Second')

# print('Start')
# second()
# first()
# print('End')

# Create a function named show_welcome
# that displays Welcome to our school!.
# Call it twice.
# Create another function named
# show_rules that displays three classroom rules.
# Call show_rules() before show_welcome()
# and observe the output order.

# def showWelcome():
#     print("Welcome to our school")

# def showRules():
#     print("Three classroom rules")

# showRules()
# showWelcome()
# showWelcome()

# def calculate_percenatge(marks): #marks is a parameter
#   percentage = marks / 500 * 100
#   print(percentage)

# calculate_percenatge(430)
# calculate_percenatge(390)
# calculate_percenatge(455)

# def calculate_percenatge(marks,total): #marks is a parameter but this time i give 2 parameters
#   percentage = marks / total * 100
#   print(percentage)

# calculate_percenatge(480,500)
# calculate_percenatge(520,600)

# def introduce(name,city):
#   print(name,'lives in',city)

# introduce('Ali','Karachi')

# create a function calculate_total that receives
# price
#quantity
# it must calculate and display the total cost

# def calculateTotal(price, quantity):
#     print(price * quantity)

# calculateTotal(400, 3)

# def check_results(marks):
#   if marks >= 50:
#     print('Pass')
#   else:
#     print('Fail')

# check_results(65)

# write check_temperature(temperature).
# Below 20: display Cold.
# From 20 through 30: display Comfortable.
# Above 30: display Hot.