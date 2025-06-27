multiplier = 1


def factorial(n):
    if n == 1:
        return 1
    else:
        mul = n*factorial(n-1)
    return mul


print(factorial(5))
