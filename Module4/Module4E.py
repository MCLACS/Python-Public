# termial width in caracters
SCREEN_WIDTH = 80

#############################################
# Returns the average of the three numbers
# passed to the function as paramaters
#############################################
def average(x1, x2, x3):
    ave = (x1 + x2 + x3) / 3
    return ave

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
 
#############################################
# Prints the specified string so it is 
# centered in the terminal
#############################################
def center(txt):
                 
    # calculate the space on each side of
    # the printed text, note that integer
    # division is used...
    num_spaces = (SCREEN_WIDTH - len(txt)) // 2
    spaces = ""

    # determine the number of spaces...
    for i in range(0, num_spaces):
        spaces = spaces + " "
    
    # print the text with the preceeding spaces...
    print(spaces + txt)
    
    # no need to return a value...
    return;

#############################################
# Calculates the largest of three numbers
#############################################
def largest(a1, a2, a3):
    
    l = 0
    
    if a1 > a2 and a1 > a3:
        l = a1
    elif a2 > a1 and a2 > a3:
        l = a2
    else:
        l = a3
        
    return l