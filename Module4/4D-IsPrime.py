#############################################
# The program's main function, don't forget
# to call it at the bottom of the file!
#############################################
def main():
    
    # get a number from the user...
    i = int(input("Enter a number: \n"))
    
    # print the string centered...
    if isPrime(i):
        print("%d is prime!" % i)
    else:
        print("%d is not prime!" % i)
        
#############################################
# Returns True if the specified integer is
# prime, otherwise it returns false
#############################################
def isPrime(num):
    
    # assume the number is prime...
    prime = True
    
    # now try and prove it is not prime
    for x in range(2, num):
        if num % x == 0:
            prime = False
            # break kicks us out of the loop...
            break 

    # return the result...
    return prime;

# Call main to kick off the program...
main()
 

