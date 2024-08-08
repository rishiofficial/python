def firstnatnum(n):
    # Base case: when n is 1, the sum is just 1
    if n == 1:
        return 1
    # Recursive case: sum of first n natural numbers is n plus sum of first (n-1) natural numbers
    else:
        return n + firstnatnum(n - 1)

print(firstnatnum(5))
