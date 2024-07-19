# a= 5
# b = 6
# print(a+b)

def sum(a,b):
    return a+b
# print(sum(5,5))

def remainder(a):
    return a%2
# print(remainder(8))

def average(a,b):
    return (a+b)/2
# print(average(4,6))

def square(a):
    return a*a
# print(square(5))

# name = input("Enter your name: ")
# print("Good afternoon" , name)

list1= [1,2,3,4]
list2 = [5,6,7,8]
# list1.extend(list2)
# list1.append(list2)
# list3 = list1 + list2
# for i in list2:
    # list1.append(i)

list1.insert(2,20)
list1.remove(20)
list1.reverse()
list1.sort()
# list1.clear()
# print(list1)

fruits = ('apple', 'banana','cherry')
(green, yellow, red) = fruits
# print(green)

# print(fruits[1])

# mytuple = ('apple', 'banana', 'cherry')
# print(type(mytuple))

# fruits = ('apple','banana','cherry','papaya','pineapple','mango')
# for i in range(len(fruits)):
#     # print(fruits[i])

def fib(num):
    if num<0:
        
        print("Enter a positive number ")
    elif num==1:
        print(0)
    else:
        a=0
        b=1
        print(a)
        print(b)
        for i in range(2,num):
            c= a+b
            a=b
            b=c
            print(c)

# num = int(input("Enter a number: "))
# fib(num)


#Factorial using recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
result = fact(5)
# print(result)

class Person:
    def __init__(self,name,age):
        self.name= name 
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

    def myfunc1(self):
        print("Hello my age is " + str(self.age))


p1 = Person("John",36)
Person.myfunc(p1)
Person.myfunc1(p1)
def fib(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,num):
        c= a+b
        a=b
        b=c
        print(c)


fib(12)
# print(x)