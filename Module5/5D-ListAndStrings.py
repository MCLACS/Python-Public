from Module5 import populateListFromUser

def main():
    
    s = "ABC123"
    myList = []
    
    populateListFromUser(myList)

    print("Printing string has %d characters." % len(s))

    print("Printing list has %d characters." % len(myList))

    print("Printing string using range and index:")
    for i in range(0, len(s)):
        print(s[i])

    print("Printing list using range and index:")
    for i in range(0, len(myList)):
        print(myList[i])

    print("Printing string using iterator:")
    for item in s:
        print(item)

    print("Printing list using iterator:")
    for item in myList:
        print(item)

    if ('A' in s):
        print("'A' is in string")

    if (4 in myList):
        print("4 is in list")
  
# Call main to kick off the program...  
main()


