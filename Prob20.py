def factorial(n):
    factorial = 2
    for num in range(3, n+1):
        factorial = factorial * num
    return factorial

def sumOfDigits(num):
    numAsString = str(num)
    sum = 0

    for digitAsChar in numAsString:
        digit = int(digitAsChar)
        sum += digit

    return sum

print sumOfDigits(factorial(100))
