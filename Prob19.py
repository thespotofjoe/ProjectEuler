nonLeapYear = [31,28,31,30,31,30,31,31,30,31,30,31]
leapYear = [31,29,31,30,31,30,31,31,30,31,30,31]

monthsLengths = []

# Generate an array with the length of all the months in the 20th century
for year in range(1901,2001):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                for length in leapYear:
                    monthsLengths.append(length)
                #print str(year) + " was a leap year."
            else:
                for length in nonLeapYear:
                    monthsLengths.append(length)
                #print str(year) + " was NOT a leap year."
        else:
            for length in leapYear:
                monthsLengths.append(length)
            #print str(year) + " was a leap year."
    else:
        for length in nonLeapYear:
            monthsLengths.append(length)
        #print str(year) + " was NOT a leap year."

sundayDate = 6
monthIndex = 0
sundayFirstCounter = 0

# Iterate through each week, detecting if the Sunday is on the first or not
while monthIndex < len(monthsLengths):
    monthLength = monthsLengths[monthIndex]
    sundayDate = sundayDate + 7

    if sundayDate > monthLength:
        sundayDate = sundayDate % monthLength
        monthIndex += 1

    if sundayDate == 1:
        sundayFirstCounter += 1

    #print "monthLength: " + str(monthLength)
    #print "sundayDate: " + str(sundayDate)

print sundayFirstCounter
