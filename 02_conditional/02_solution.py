
# age = input("Provide me your age: ")
# age = int(age)

# if age < 18:
#     print("Give me $8 for movie ticket")
# else:
#     print('Give me $12 for movie ticket')

# day = "Wednesday"

# if day == "Wednesday":
#     print("Everypne get a discount 🎉")
# else:
#     print("No discount please!")


age = 26 
day = "Wednesday"

price = 12 if age>= 18 else 8

print(price)

if day == "Wednesday":
    price = price -2

print("Ticket price for you is $", price)