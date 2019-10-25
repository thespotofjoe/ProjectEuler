primes = [2,3,5,7,11,13,17,19]

def isPrime(possiblePrime):
    for x in range(2,int(round(possiblePrime/2)-1)):
        if possiblePrime % x is 0:
            return False;
        
    return True;

testNumber = 19

while len(primes) < 10001:
    testNumber += 2
    if isPrime(testNumber):
        primes.append(testNumber)

print("The 10,001st prime number is: ",testNumber)
