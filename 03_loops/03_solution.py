number = 3

for i in range(1,11):
    if i == 5:
        continue
    print(number, 'X', i,'=', number * i )


#solution_4
    
fruit = "Banana"
reverse_string = ""

for i in fruit:
    reverse_string = i + reverse_string 
print(reverse_string)

#Solution_5

for char in fruit:
    if fruit.count(char) == 1:
        print(char)

#Solution_6
        
number = 5
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(factorial)

#Solution_7
# while True:
#     number = int(input("Enter a number between 1 and 10: "))
#     if 1<= number <= 10:
#         print("Thanks🤗")
#         break
#     else:
#         print("Invalid value , please enter again")


    




