def isPalindrome (n):
    i = 2
    while 10**i < n:    #Find the number of digits in the number n

    j = 0
    while i != j:
        if n%10**i != n%10**j:  #Figure out whether the digit at i is the same as
            return False        #the digit at j, if not, return false
        i -= 1
        j += 1
        
    return True

def main(n):
    if isPalindrome(n):
        print(n, " is a palindrome.")
    else
        print(n, " is not a palindrome.")

if __name__ == "__main__":
    for i in range(101,9999):
        main(i)
