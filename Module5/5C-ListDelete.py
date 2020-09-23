from Module5 import populateListFromUserNoDups

def main():
    myList = []
    
    populateListFromUserNoDups(myList)
    
    print("List has %d items." % len(myList))

    print("List: %s" % myList)
    
    # remove the second item in the list
    removedItem = myList.pop(1)    
    print("List after removing second item using pop: %s" % myList)

    # remove first instance of 7 from list
    removedItem = myList.remove(7)    
    print("List after removing first instance of 7 using remove: %s" % myList)
    
    del myList[0]
    print("List after removing first item in list using del: %s" % myList)

# Call main to kick off the program...  
main()


