# Take a input number
# Match with the randomly generated data
# If matched give the result
import random


random_number = random.randrange(1,100)
print("Enter the number between 1 and 100 and have only 5 attempts")
print(random_number)

# for num in str(random_number):
#     if num == number:
#         print("Number matched successfully")
#     else:
#         print("Try again")
#         print(input("Enter the number again: "))
attempt_count =  0
max_attempt = 5

while attempt_count<max_attempt:
    attempt_count +=1
    number = int(input("Enter the guessed number: "))
    if attempt_count<max_attempt:
        if number == random_number:
            print("Number matched successfully")
            break
        elif 10<= random_number<=20:
            print("Number is greater than 10 and less than 20")
        elif 20<= random_number<=30:
            print("Number is greater than 20 and less than 30")
        elif 30<= random_number<=40:
            print("Number is greater than 30 and less than 40")
        elif 40<= random_number<=50:
            print("Number is greater than 40 and less than 50")
        elif 50<= random_number<=60:
            print("Number is greater than 50 and less than 60")
        elif 60<= random_number<=70:
            print("Number is greater than 60 and less than 70")
        elif 70<= random_number<=80:
            print("Number is greater than 70 and less than 80")
        elif 80<= random_number<=90:
            print("Number is greater than 80 and less than 90")
        elif 90<= random_number<=100:
            print("Number is greater than 90 and less than 100")
        else: 
            print("Try AGAIN")
    else:
        print(f"You run out of your attempt,the correct number is {random_number}")