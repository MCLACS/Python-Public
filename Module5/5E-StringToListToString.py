from Module5 import listToString
from Module5 import stringToList

def main():
    
    s = "ABC123"
    l = stringToList(s)
    print("Printing list %s" % l)

    l = ['A', 3, 'Z', 9]
    s = listToString(l)
    print("Printing string '%s'" % s)
  
# Call main to kick off the program...  
main()



