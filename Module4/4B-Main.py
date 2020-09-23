#############################################
# The program's main function, don't forget
# to call it at the bottom of the file!
#############################################
def main():
    
    # get three numbers from the user...
    num1 = int(input("Enter number 1: \n"))
    num2 = int(input("Enter number 2: \n"))
    num3 = int(input("Enter number 3: \n"))

    # calculate the average...
    a = average(num1, num2, num3)

    # print the average...
    print("Average: %.2f" % a)
    
#############################################
# Returns the average of the three numbers
# passed to the function as paramaters
#############################################
def average(x1, x2, x3):
    ave = (x1 + x2 + x3) / 3
    return ave

main()
