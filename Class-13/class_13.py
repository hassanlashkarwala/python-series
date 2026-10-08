# Practice / Revision old topics

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])
# -1 last element return karega 

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# 2 element se start ho and 5 se phele element pe stop waha tak list return kro mujhe

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])
# ye start 0 element se hoga bcz kuch starting point nh diya wo khud hi first element se start kare ga

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# -1 ko hum last element khete hen!

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if "orange" in thislist:
#     print("Yes, 'orange' is in the fruits list")

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# is question me ye hoga ke apple print hoga phr blackcurrant watermelon ai ga and banana and cherry gayab bcz : 3 diya hua hai 3 se phele stop hona hona hai tw 2 elements delete ho jai gay

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
# insert ke baad ab mene 2 likha hai wo second index pe add kr dega element ko agar me tw ki jagah 5 bh deta ho halake list me index number 5 hai bh nh phr bh wo mujhe koi error nh dega balke list ke end me add kr dega wo wala element
# insert ka method humse 2 arguments maangta hai, aik tw wo point jaha apko list me us cheez ko add krna hai and second argument me ju add krna hai uska name

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
# append array ke last me element ko add karega

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
# extend method 2 lists ko aps me join karta hai!

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("apple")
# print(thislist)
# remove method apke array me se us element ko remove krwai ga jiska apne name call krwaya hoga

# Remove Specified Index: The pop() method removes the specified index.
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)
# agar me pop method me koi index number deta ho tw wo us index number wale element ko remove kr dein ga and agar me index number nh deta tw wo array me se last element ko remove kr dega

# The del keyword also removes the specified index:
# thislist = ["apple", "banana", "cherry"]
# del thislist[1]
# print(thislist)
# del keyword se bh hum array ke element ko delete krwa sakte hen

# Now learn list with loop
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# thislist = ["apple", "banana", "cherry"]
# for list in range(len(thislist)):
#     print(thislist[list])

# A short hand for loop that will print all items in a list:
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# practice question, list me dekho jis element me a keyword araha hai usko ap new list me add kr do
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [];

for list in fruits:
    if "a" in list:
        newList.append(list)
print(newList)