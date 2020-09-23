from Module5 import populateListFromUser

def main():
    myList = []
    
    populateListFromUser(myList)
    
    print("List has %d items." % len(myList))

    print("Printing list using range and index:")
    for i in range(0, len(myList)):
        print(myList[i])

    print("Printing list using iterator:")
    for item in myList:
        print(item)
    
    print("Printing list using string conversion: %s" % myList)

    myList.sort()
    
    print("Printing list after sorting: %s" % myList)

  
# Call main to kick off the program...  
main()

