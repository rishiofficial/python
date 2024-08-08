#Both the players should keep the gestures simultaneously. The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#logic
#first we use random built in function in python and then use if-else statment for different cases.


import random


# print(game)
# user_input = input("Enter: ")
# if game == user_input:
#     result = "The game is draw"
# elif game == 'snake' and user_input == "water":
#     result = "Computer wins🎉"
# elif game == 'gun' and user_input == "snake":
#     result = "Computer wins🎉"
# elif game == "water" and user_input == "snake":
#     result = "User wins🎉"
# elif game == "water" and user_input == 'gun':
#     result = "Computer wins 🎉"
# elif game == "gun" and user_input == 'water':
#     result = 'User wins🎉'
# elif game == "snake" and user_input == 'gun':
#     result = "User wins🎉"
# else:
#     result = "Please enter valid details"

# print(result)

def gamewin(comp, user):
    if comp == user:
        return "The game is draw"
    elif (comp == 's' and user == 'g') or (comp == 'g' and user=='w') or (comp == 'w' and user =='s'):
        return "User wins 🎉"
    else: 
        return "Computer wins 🎉"
    

choices = ['s','g','w']
comp = random.choice(choices) 

user = input("Enter snake(s) ,water (w) and gun(g)/n Enter your choice: ").lower()

if user not in choices:
    print("Invalid choice, please enter 's', 'w', or 'g'.")
else:
    result = gamewin(comp, user)
    print(f"\nComputer chose: {comp}")
    print(f"You chose: {user}")
    print(result)

computer_score = 0
user_score = 0
if result == "Computer wins 🎉":
    computer_score += 1
elif result == "User wins 🎉":
    user_score+=1


print(computer_score)
print(user_score)