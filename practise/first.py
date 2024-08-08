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

# class Person:
#     def __init__(self,name,age):
#         self.name= name 
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)

#     def myfunc1(self):
#         print("Hello my age is " + str(self.age))


# p1 = Person("John",36)
# Person.myfunc(p1)
# Person.myfunc1(p1)
# def fib(num):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,num):
#         c= a+b
#         a=b
#         b=c
#         print(c)


# fib(12)
# print(x)

import datetime

name = "Rishikesh"
date = datetime.datetime.now()

x = f''' Dear {name} you are selected  in {date.year}'''

# print(x.strip())
#chapter 4
fruits = ['Mango','Banana','Guava', "Apple",'pineapple','coconut','pomogrenate']
marks = [50,45,67,40,90]
marks.sort()
# print(marks)

marks = (45.60,75,89,50)
# marks[0] = 45
# print(marks) tuple cannot be changed

list = [40,50,10,20]
y = 0
for x in list:
    y += x

# print(y)

a =(7,0,8,0,0,9)
b=a.count(0)
# print(b)

#chapter 5
dict = {
    "Aam": "mango",
    "kitab": "book",
    "pasand": "like"
}
print(dict.values())

# num = input("Enter 8 number: ")
# print(num)

my_set = {18,"18"}
# print(type(my_set))

s= set()
s.add(20)
s.add(20.0)
s.add("20")
# print(len(s))
s={}
# print(type(s))

#if the name of the two friends are same then it overwrite the another one, keys must be unique whereas values can be multiple 

# num= 77
# if num%7==0:
#     print(f"{num} is a multiple of 7")
# else:
#     print("not multiple number")

# x = int(input("please enter a number: "))
# for i in range(1,11):
#    num = i*i
#    if num == x:
#         print("found")
#    else:
#         print("not found")
#         break





num = 5 
factorial = 1
while num>0:
    factorial = factorial*num
    num = num -1
print(factorial)
