# name = input("Enter your name here: ")
# marks = int(input("Enter your marks here: "))
# print(name, marks)

# file = open("student.txt", "w") #  w for write
# file.write("Ali")
# file.close()
# print("Information saved successfully")

# create a file named about_me.txt with your name, city
# programming language that you are learning 
# f = open("aboutme.txt", "w") 
# f.write("My name is hassan")
# f.write("I live in Karachi")
# f.write("I'm learning python")
# f.close()
# print("Info saved")

# file = open("aboutme.txt", "r")   #  r for read
# content = file.read()
# print(content)
# file.close()

# file = open("subjects.txt", "w")
# file.write("Python\nMaths\nCS\nBiology")
# file.close()
# print("successfully")

# file = open("subjects.txt", "r")
# first_line = file.readline()
# second_line = file.readline()
# file.close()
# print(first_line)
# print(second_line)

# f = open("scores.txt", "w")
# f.write("70\n85\n90\n65")
# f.close()
# f = open("scores.txt", "r")
# content = f.read()
# print(content)
# f.close()

# abc = open("subjects.txt", "r")
# subjects = abc.readlines()   #create list with the help of readlines
# print(subjects)
# abc.close()

# remove \n from the name of each subject
# new_subjects = []
# for subject in subjects:
#     subject = subject.strip()
#     new_subjects.append(subject)
# print(new_subjects)

# how many lines are there in subjects file

# f = open("subjects.txt", "r")
# count = 0
# for line in f:
#     count += 1
# f.close()
# print("numbers of lines: ", count)

# agar doo file aik hi name ki hogi, tw ju second file hai wo file file ke content ko over write kr dei gi

# three modes of file handling
# "r":  read existing information
# "w":  write, replacing existing content
# "a":  appends information at the end

with open("message.txt", "w") as file:
    file.write("ABC")
    file.write("\nDEF")
print("Saved")