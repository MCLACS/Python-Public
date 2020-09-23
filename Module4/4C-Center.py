# termial width in caracters
SCREEN_WIDTH = 80

#############################################
# The program's main function, don't forget
# to call it at the bottom of the file!
#############################################
def main():
    
    # get a string from the user...
    s = input("Enter a string: \n")
    
    # print the string centered...
    center(s)
        
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

# Call main to kick off the program...
main()
 
