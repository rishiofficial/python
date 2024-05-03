
def myfunc(number):
    print(number ** 2)
myfunc(4)

#solution_2
def sum(x,y):
    return x+y
result = sum(4,5)
print(result)

#solution_3

def product(x,y):
    return x*y
result = product("mango",5)
print(result)

#solution_4
import math
def area_circum(radius):
      area = int(3.14 * radius** 2) 
      circum = (int(math.pi * 2* radius))
      return area,circum
a,c =area_circum(7)
print(a,c)