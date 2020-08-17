# Program to calculate ProjectEuler.net Problem 12 - find the first triangle number
# with over 500 factors.

def generateTriangleNumber(prev, nextNum):
    return(prev + nextNum)

def isAFactor(potentialFactor, number):
    return (number % potentialFactor == 0)

number = 1
tally = 0
triangleNumber = 0

# I made the talley 498 to account for the factors 1 and the number itself,
# which I don't add to the tally
while (tally <= 498):
    tally = 0
    triangleNumber = generateTriangleNumber(triangleNumber, number)

    # I first tried to find all factors between 2 and num/2+1, and then add 2
    # for the number and 1 itself but it was taking too long I realized
    # I only needed to find the factors between 2 and the square root,
    # then double what I found and add 2. Instead of hours and hours
    # it only took a minute to find the correct answer
    for potentialFactor in range(2, int(triangleNumber ** 0.5) + 1):
        if (isAFactor(potentialFactor, triangleNumber)):
            tally += 2

    print ("Update:")
    print (triangleNumber)
    print (tally)
    print ("")

    number += 1

print ("Found it!")
print (triangleNumber)
print (tally)