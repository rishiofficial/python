# need input area for entering the number for calculation
# WRITE A function to calculate for all operation 

def addition(num1,num2):
     return num1 + num2

def subtraction(num1,num2):
   return  num1-num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1/num2


    #  input("Enter the number: " num1,num2)
while True:
    print("1.Add the number")
    print("2.subtract the number")
    print("3.multiply the numbers")
    print("4.divide the number")
    print("5.Exit the app")
    
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1','2','3','4','5'):
        num1 = float(int(input("Enter the first number: ")))
        num2 = float (int(input("Enter the second number: ")))    

        if choice == "1":
                print("result:", addition(num1,num2))
        elif choice =="2":
                print("result: ",subtraction(num1,num2))
        elif choice == "3":
                print("result: ", multiplication(num1,num2))
        elif choice =="4":
                print("result: ", division(num1,num2))
        elif choice == "5":
                print("Thanks for using calculator")   
                break
    else:
        print("Invalid input")    

    # match choice :
    #     case '1':
    #         print("result", addition(num1,num2)) 
    #     case '2':
    #         print(f"result", subtraction(num1,num2))

       
