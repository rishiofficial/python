#solution_9

def even_genrator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even_genrator(10):
    print(num)

def factorial(n):
    if n == 0:
        return n
    else:
        return n * factorial(n-1)