#The problem asks the sum of the digits of 2^1000
numAsString = str(2**1000)
sum = 0

for digitAsChar in numAsString:
    digit = int(digitAsChar)
    sum += digit

print sum
