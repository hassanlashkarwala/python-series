# Again solved the last question!
# age = int(input("Enter your age here: "))

# if age >= 18:
#     passport = input("Do you have a passport? ")
#     if passport == "yes":
#         ticket = input("Do you have a ticket? ")
#         if ticket == "yes":
#             luggage = input("Is your luggage less than 30kg? ")
#             if luggage == "yes":
#                 print("Check in sucessfull")
#             else:
#                 print("Extra baggage fees will apply")    
#         else:
#             print("You dont have a ticket")    
#     else:
#         print("You don't have a passport")
# else:
#     print("Are you under 18")     

# ab agar 5 bar apna name likhna hai tw?
# ab aik tareeqa ye hai ke 5 baar name print krwa do
# print("Hassan")
# print("Hassan")
# print("Hassan")
# print("Hassan")
# print("Hassan")

# now we learn loops!
# We have two types of loops 
# for loop
# while loop

# for loop syntax
# for i in range()

# for keyword hai python ka
# in bh keyword hai python ka
# the in keyword in python acts like a search tool to check if a specific value ...
# aik cheez ko bar baar repeat krna hai tw me loop ka use krta ho
# i: is a variable
# range(10): provide the sequence of repetitions

# ab apna name 5 baar print krwana hai with the help of for loop
# for i in range(10):
#     print("Hassan")

# ab me chahta ho ke i ki value dekho! and zaroori nh i hi do me, me yaha a, b, c kuch bh de sakta ho
# for i in range(5):
#     print(i)

# ab agar sirf me likhta ho range()
#print(range(5))  # ye mujhe ye return kre ga range(0, 5)  

# for i in range(3):
#     print("Hello", i);

# print numbers from 0 to 9 using for loop
# for i in range(10):
#     print(i)

# print "python is fun" ten times
# for i in range(11):
#     print("python is fun")    

# ab range me two values pass kare gay means range(start, stop); 
# starting point ju dena chahe app and ending point bh ap ju dena chahe
# de sakte hen    

# for i in range(1, 7):
#     print(i)

# one more thing in range 
# total three things
# range(start, stop, step)
# ab start tw ye kr raha hai apka number kaha se start ho raha
# ending point end bata raha hai
# step ye karta hia ke agar apne likha step 1 tw wo normally hi run hoga 1, 2, 3, 4
# but me likhoga step 2 tw wo 1 ke baad 1 aur ko choore ga 3 pe ajai ga yuh
 
# for i in range(1, 10, 2):
#     print(i)

# ab for loop ke zarye se reverse counting with the use of start stop & step
# for i in range(10, 0, -1):
#     print(i) 
# iska output mere pass 10 se 1 tak ayaa hai
# ab mujhe output chahiye 10 se 0 tak tw ab mujhe stop point ju hai -1 dena hoga
# jab ja kr wo stop hoga 0 pe

# for i in range(10, -1, -1):
#     print(i) 

# print even numbers from 2 to 20 using for loop and range
# for i in range(2, 21, 2):
#     print("Even numbers", i)

# print odd numbers from 1 to 19
# for i in range(1, 20, 4):
#     print("Odd numbers", i)

# for i in range(2, 20, -2)   me agar yuh likhoga tw kuch bh output nh aiga


# Loops + arithmetic
# for i in range(1, 11):
#     print(i * 2)

# ask user for a number and print its table from 1 to 10
# output format: ex: 4 x 1 = 4
# do it using for loop

table = int(input("Enter which table you want? "))
for i in range(1, 11):
    print(table, "x" , i, "=", i * table)    