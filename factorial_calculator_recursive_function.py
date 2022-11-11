# recursive function (function calls itself)
# factorial calculator

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = factorial(int(input("Your number: ")))

print(number)


