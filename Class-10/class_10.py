# add all marks and print total
# marks = [75,83,61,73,93]
# total=0
# for i in marks:
#     total = total + i;
# print(total);

# students = ["ahmed", "sara", "ali", "usman", "ayesha"]
# now we learn slice!
# array me se kitne elemene apko chahiye wo bata do bs
# students_slice = students[0:3]  # tw ab mere pass 0 se start and end hoga 3 but 3 wale ko print me add nh krega wo
# print(students_slice);

# this slice will contain values of index 1, 2, 3
# numbers = [10, 20, 30, 40, 50, 60];
# print(numbers[1:4]);

# acha yaha pe aik benefit hota hai slice me ke agar app start se hi shoro krna chahte hen [tw appko 0 bh likhne ki need nh]
# numbers[:3]  # ab jese mene yaha beginning value nh di 0 wo khudi 0 se start krega element lena and end krega 3 se phele phele

# one more benefit agar mene starting point bata diya bs and me chahte ho aagey ke sab elements mil jai mujhe
# numbers[2:]  # ab ye 2 se start and end tak chale ga

# numbers[:] 
#numbers   # boths are same mujhe array ke sab elements mil jai gay isse bh and upper wale code se bh

# slice the last 3 items of numbers list
# numbers = [10, 20, 30, 40, 50, 60];
# lastThree = numbers[-3:];
# print(lastThree)

# now we used in!
# students = ["ahmed", "sara", "ali", "usman", "ayesha"]
# checkSomething = "Noman" in students;  # false bcz Noman is not defined in an array
# checkSomething = "usman" in students;    # true
# print(checkSomething);

# write a code which takes name as input from user
# check the name in students list
# print student found or not found
# name = input("Enter a name here: ")
# studentsList = ["Ali", "Hassan", "Ahmed", "Shayan"];

# if name in studentsList:
#     print("Found");
# else:
#     print("Not found!");

# ask user for a number and find it in a list
# numbers = [20, 30, 40, 50]
# askUserForNumber = int(input("Enter a number here: "));

# if askUserForNumber in numbers:
#     print("Found");
# else:
#     print("Not found");

# count number of 10's in the list
# numbers = [10, 20, 30, 40, 50, 10]
# count = 0
# for i in numbers:
#     if i == 10:
#         count = count + 1;
# print(count);

# ab ye cheez asan hai ke ab mujhe count karna hai aik hi element kitni baar ayaa hai in array
# tw mere pass aik method hai count
# print(numbers.count(10));
# ab ye dekhe ga ke numbers ka ju array hai iske andar 10 kitni bar hai apko count kr ke bata dei ga

# now we learn insert method app array me isko kahi bh insert krwa sakte ho
# numbers.insert(2, 120);
# print(numbers);

# now we can sorting the array element
# numbers = [10, 20, 30, 50, 40, 10]
# numbers.sort();
# print(numbers);

# letters = ["r", "p", "t", "a", "c"];
# letters.sort();
# print(letters);

# letters.sort(reverse=True)
# print (letters)
# same method goes for the numbers

# now we can learn reverse method!
# numbers = [10, 20, 30, 50, 40];
# numbers.reverse();
# print(numbers);

# Find the average of these numbers

# find total price
# find most expensive
# find cheapest
# how many products are there
prices = [250, 500, 1200, 750, 100];