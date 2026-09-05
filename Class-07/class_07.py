# for loop

# for i in range(5):
#     print(i);

# for i in range(2, 8):
#     print(i)

# for i in range(1, 6):
#     print(i * 10)

# reverse counting hogi yaha! bcz last step me -2 araha hai
# for i in range(10, 0, -2):
#     print(i)

# write a code to sum first 5 numbers
# number = 0
# for i in range(1,6):
#     number = number + i
#     print(number)
# yaha imp bat! agar me intend khatam kr deta ho tw for loop se bahir aik tareeqa se aik sirf aik ouput aii ga last wala means 15
#  and agar intend rehne deta ho, tw har aik value ka ouput ai ga console me

# write a code to sum first 10 numbers
# number = 0;
# for i in range(1, 11):
#     number = number + i 
# print(number)

# user = int(input("Enter which number you want to sum: "));

# for i in range(1, user+1):
#     user = user + i
# print(user)  

# find the sum of all even numbers between 1-100
# sum = 0;
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)

# count the even numbers from 1 to 20
# count = 0
# for i in range(1,21):
#     if i % 2 == 0:
#         count = count + 1
# print(count)

# count numbers divisible by both 3 & 5 between 1 and 100
# numbers = 0;
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#       numbers += 1  # numbers = numbers + 1 boths are same ye bh likh sakta ho and comment se phlee ju likha hai wo bh right h
# print(numbers)

# ask user for number of students add the marks of each student
# students = int(input("Enter your students here: "))
# total = 0
# for i in range(students):
#    marks = float(input("Enter your marks here: "))
#    total += marks
# print("Total Marks", total)
# print("Average Marks", total/students)

# user se students lo and marks pocho student ke student ke marks 50 se kam ho tw usko bol dena are you failed and 50 se ziada marks ho uske tw wo passed hai
# students = int(input("Enter your students here: "))
# total = 0
# passed = 0
# failed = 0
# for i in range(students):
#    marks = float(input("Enter your marks here: "))
#    total = total + marks
#    if marks >= 50:
#       passed = passed + 1
#    else:
#       failed = failed + 1
# print("Total", total)
# print("passed", passed)
# print("failed", failed)
# print("Average Marks", total/students)

# Practice Questions
# ask user for 5 numbers and find the largest of those