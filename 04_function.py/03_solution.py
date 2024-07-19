#solution_9

# def even_genrator(limit):
#     for i in range(2,limit+1,2):
#         yield i

# for num in even_genrator(10):
#     # print(num)

def factorial(n):
    f=1

    for i in range(1,n+1):
        f =f*i
    return f
x=5
result= factorial(x)
print(result)

# factorial using recursion


