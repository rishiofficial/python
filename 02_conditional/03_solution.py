# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# marks = 89

# if marks<=100 and marks >= 90:
#     print("The grade of student is A")
# elif marks <=89 and marks >=80:
#     print("The grade of student is B")
# elif marks <= 79 and marks >=70:
#     print("The grade of student is C")
# elif marks <= 69 and marks >= 60:
#     print("The grade of student is D")
# else:
#     print("The grade of student is F")

score = 101
if score >= 101:
    print("Please verify your grade")
    exit()

if score>= 90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'F'

print(grade)
