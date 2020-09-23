from Module4E import largest
from Module4E import average

def main():
     
     # get three numbers from the user...
    num1 = int(input("Enter number 1: \n"))
    num2 = int(input("Enter number 2: \n"))
    num3 = int(input("Enter number 3: \n"))
    
    large = largest(num1, num2, num3)
    print("Largest is %d" % large)
    
    a = average(num1, num2, num3)
    print("Average is %.2f" % a)
    
main()