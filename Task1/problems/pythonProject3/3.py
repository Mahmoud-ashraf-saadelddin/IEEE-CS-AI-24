def factorial(n):
    if (n == 1):
        return 1
    else:
        return (n * factorial(n - 1))


n = int(input())
if n > 0:
    print(f"The factorial of {n} is {factorial(n)}")
else:
    print("that is not valid number ")
