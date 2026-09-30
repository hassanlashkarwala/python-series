# Task 1 — Supermarket Checkout System

# You are developing a simple checkout program for a supermarket. A customer can buy multiple products. First ask how many different products the customer has purchased.
# For every product, ask for: product name, price and quantity.

# How many products? 3

# Product 1
# Name: Milk
# Price: 250
# Quantity: 2

# Product 2
# Name: Bread
# Price: 180
# Quantity: 1

# Product 3
# Name: Eggs
# Price: 320
# Quantity: 2
# For every product calculate: Item total = Price × Quantity.
# Then calculate the subtotal for the entire bill.
# Subtotal	Discount
# 10,000 or more	10%
# 5,000–9,999	5%
# Below 5,000	No discount
# Final Bill = Subtotal - Discount
# Display a clear receipt similar to:
# ================================
#         SUPERMARKET BILL
# ================================

# Milk        2 x 250 = 500
# Bread       1 x 180 = 180
# Eggs        2 x 320 = 640

# Subtotal: 1320
# Discount: 0
# Final Bill: 1320

# Thank you for shopping!
# ================================
# Requirements:
# •	Use input(), int() and/or float() as appropriate.
# •	Use a loop to collect the products.
# •	Use arithmetic and if/elif/else for the discount.
# •	Use at least one list.
# •	Do not hard-code the final totals.
# •	Extra challenge: keep product names and calculated item totals in lists and use those lists to display the receipt

# userProduct = input("Enter your product here: ");
# productPrice = int(input("Enter your product price here: "))
# productQuantity = int(input("Enter your product quantity here: "))
# totalItem = productPrice * productQuantity
# print(totalItem)

# if totalItem >= 10000:
#     discountTenPercent = totalItem * 0.10;
#     finalBill = discountTenPercent;
#     print(totalItem);
#     print(discountTenPercent);
#     print("Discount 10 percent for you, thanks!", finalBill);
# if totalItem >= 5000 and totalItem < 10000:
#     discountFivePercent = totalItem * 0.05;
#     finalBill = discountFivePercent;
#     print(totalItem)
#     print(discountFivePercent);
#     print("Discount 05 percent for you, thanks!", finalBill);
# if totalItem < 5000:
#     print("Discount: 0")
#     print("No discount because your bill is below 5000, thank you!", totalItem);

number_of_products = int(input("How many products? "))
products_names = [];
total_items = [];

for i in range(number_of_products):

    addProductName = input("Enter your product name here: ");
    addQuantity = int(input("Enter your product quantity here: "));
    productPrice = float(input("Enter your product price here: "))

    itemTotal = productPrice * addQuantity;
    products_names.append(addProductName)
    total_items.append(itemTotal)

subtotal = sum(total_items);
print("This is your total bill", subtotal);

if subtotal >= 10000:
    discount = subtotal * 0.10;
    print("Your discount of 10%", discount);
elif subtotal >= 5000 and subtotal < 10000:
    discount = subtotal * 0.05;
    print("Your discount of 5%", discount);
else:
    discount = 0;
    print("No discount because your bill is less than 5000", subtotal) 

finalBill = subtotal - discount;
print("Final Bill: ", finalBill);