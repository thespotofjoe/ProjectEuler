for c in range (333, 998):              #cycle through all possible c's
    
    for a in range (1, int(round(c/2))):#cycle through all possible a's for this c
        b = 1000 - c - a                #set b so the sum of all 3 is 1,000
        #print "A: ", a, "\nB: ", b, "\nC: ", c #debug
        #print "a*a + b*b: ", a*a+b*b, " c*c: ",c*c #debug
        
        if (a**2 + b**2) == c**2:
            print "Eureka! A: ", a, "\nB: ", b, "\nC: ", c

print "done"
