# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# solution - 8
password = "abcd@123"

if len(password) < 6:
    pass_strength = "Weak"
elif len(password) <10:
    pass_strength = "Medium"
elif len(password) > 10:
    pass_strength = "Strong"

print(pass_strength)

# solution - 9

year = 2025

if (year % 4 == 0) or (year % 400 == 0 and year % 100 != 0) :
   print(year," is leap year")
else:
   print(year," is not leap year")

#solution - 10
   
   pet_species = "dog"
   year = 1

if pet_species == "dog" and year <= 2:
   food = "Puppy Food"
elif pet_species == "cat" and year > 5:
   food = "Senior Cat food"

print(food)