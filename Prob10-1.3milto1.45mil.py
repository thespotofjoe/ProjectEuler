primes = []

def isPrime(possiblePrime):
    for x in range(2,int(round(possiblePrime/2)-1)):
        if possiblePrime % x is 0:
            return False;

    print "Prime found: ",possiblePrime #debug
    return True;

for x in range(1300001,1450000,2):
    if isPrime(x):
        primes.append(x)
print "Done finding primes. Adding ",len(primes)," primes now." #debug

sum = 0
for x in primes:
    sum += x

print("The sum of all primes between 1.3mil and 1.45mil is: ",sum)

input() #wait when done
