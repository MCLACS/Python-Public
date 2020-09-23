from Module4E import average
from Module4E import center
from Module4E import isPrime

def main():
    
    # get three numbers from the user...
    num1 = int(input("Enter number 1: \n"))
    num2 = int(input("Enter number 2: \n"))
    num3 = int(input("Enter number 3: \n"))
    
    # calculate the average...
    ave = average(num1, num2, num3)
    
    # print the average...
    print("Average: %.2f" % ave)
    
    center(str(ave))
    
    center(str(isPrime(7)))

# Call main to kick off the program...
main()