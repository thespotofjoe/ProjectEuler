# This problem asks how many letters are in every number from
    # 1 through 1,000, disregarding spaces and hyphens
    # and including the "and" as in "one hundred AND fourteen"

def sub20(num):
    if num == 0:
        return 0
    if num == 1:
        return len("one")
    if num == 2:
        return len("two")
    if num == 3:
        return len("three")
    if num == 4:
        return len("four")
    if num == 5:
        return len("five")
    if num == 6:
        return len("six")
    if num == 7:
        return len("seven")
    if num == 8:
        return len("eight")
    if num == 9:
        return len("nine")
    if num == 10:
        return len("ten")
    if num == 11:
        return len("eleven")
    if num == 12:
        return len("twelve")
    if num == 13:
        return len("thirteen")
    if num == 14:
        return len("fourteen")
    if num == 15:
        return len("fifteen")
    if num == 16:
        return len("sixteen")
    if num == 17:
        return len("seventeen")
    if num == 18:
        return len("eighteen")
    if num == 19:
        return len("nineteen")

def tensDigit(num):
    if num == 2:
        return len("twenty")
    if num == 3:
        return len("thirty")
    if num == 4:
        return len("forty")
    if num == 5:
        return len("fifty")
    if num == 6:
        return len("sixty")
    if num == 7:
        return len("seventy")
    if num == 8:
        return len("eighty")
    if num == 9:
        return len("ninety")

def sub100(num):
    if num < 20:
        return sub20(num)

    numAsString = str(num)

    tensDigitNum = int(numAsString[0])
    onesDigitNum = int(numAsString[1])
    return (tensDigit(tensDigitNum) + sub20(onesDigitNum))

def above100orEqual(num):
    numAsString = str(num)

    hundredsDigitNum = int(numAsString[0])

    # If we're at an even hundred, just calculate the hundred's digit
    if numAsString[1] == '0' and numAsString[2] == '0':
        return sub20(hundredsDigitNum) + len("hundred")

    # Otherwise, calculate the whole shebang plus "and"
    sub100Component = int(numAsString[1]+numAsString[2])
    return sub20(hundredsDigitNum) + len("hundred") + len("and") + sub100(sub100Component)

sum = 0
for num in range(1,1000):
    print "Calculating letters for " + str(num)
    if num < 100:
        print "It's " + str(sub100(num)) + " for " + str(num)
        sum += sub100(num)
    else:
        print "It's " + str(above100orEqual(num)) + " for " + str(num)
        sum += above100orEqual(num)

sum += len("onethousand")

print sum
