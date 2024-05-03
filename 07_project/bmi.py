# YOU NEED TWO INPUT ONE HEIGHT AND WEIGHT
# create a function that calculate the bmi
# On the basis of result we categorised result in healthy , overweight , malnourised. 

weight = float(input("Enter your weigth here in kg: "))
# print(weight)

height = float(input("Enter your height here in meter: "))
# print(height)






result = weight / (height ** 2)
print("This is your BMI",result)



if 19<= result <=25:
    print("You are healthy")
elif result > 25:
    print("You are overweight")
else:
    print("You are malnourised")

