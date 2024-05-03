#solution_5

def greet(name = "User"):
    return "Hello, " + name 
print(greet("Rishi"))

#solution_6
# def Lambda(num):
#     return num ** 3
# print(Lambda(6))

cube = lambda x: x**3
print (cube(3))

#solution_7
def argument_sum(*args):
    return sum(args)
print(argument_sum(1,2,3,4))

 #solution_8
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "shaktiman", power ="lazer")
print_kwargs(name="Shaktiman", power="lazer", enemy = "Dr Jackal")