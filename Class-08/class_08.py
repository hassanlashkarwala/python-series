# ask user to enter a password, they have unlimited
# attemps, the program should stop
# as soon as they enter correct password

# for i in range(3):
#     userPassword = input("Enter your password here: ");
#     if userPassword == "python1234":
#         print("Correct password", userPassword);

# now we can learn while loop
# i = 1;
# while i <= 5:
#     print(i);
#     i = i + 1;

# print numbers from 10 to 1 using while loop
# i = 10;
# while i >= 1:
#     print(i);
#     i -= 1;

# print even numbers from 2 to 20 using while loop
# solved two ways

# first way
# i = 2;
# while i <= 20:
#     print(i);
#     i += 2;

# second way
# i = 2;
# while i <= 20:
#     if i % 2 == 0:
#         print(i);      #iske neche ju iteration hai wo if ki condition ke bahir krni paregi!
#     i += 1;

# print multiples of 5 from 5 to 50 using while loop
# i = 5;
# while i <= 50:
#     print(i)
#     i += 5;

# password problem 
# jab tak user sahi password input me na put kare tab tak mera loop chalta jai is wajah se while loop use krna hoga
# for loop me batana par raha kitne baar chalo
# but while me hamare hand me hoti hai limit range, ke jab tak user sahi password na daal dein tum chalte raho

# password = "";
# while password != "python123":
#     password = input("Enter your password: ")
# print("Login successful");   #ye print loop ke bahir lagaya hai, taake jab user sahi password enter kr dein jabhi ye print ho warna na ho!!

# To the above program add a functionality of displaying!
# if password is incorrect so show the your password is incorrect
# password = "";
# while password != "python123":
#     password = input("Enter your password: ");
#     if password != "python123":
#         print("Your password is incorrect");
# print("Login successful");

# keep asking user for a number until they
# enter a negative number
# number = 0
# while number >= 0:
#     number = int(input("Enter number: "));
# print("Negative number entered!!!");

# sum numbers from 1 to 100 using while loop