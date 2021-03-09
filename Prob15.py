#This problem involves routes in a 20x20 grid
    #it asks how many routes can be made from the top-left corner to the bottom right
    #Each route has 20 right moves and 20 down moves, rearranged in different ways.
    #All I have to calculate is how many permutations we have of those.
    #This amounts to 40!/20!*20!
    #40! to count the permutations of each move,
    #then divide by 20! because all the d moves are the same,
    #and another 20! because all the right moves are the same.

import math

print "The number of unique routes is: "
print math.factorial(40)/(math.factorial(20)*math.factorial(20))
