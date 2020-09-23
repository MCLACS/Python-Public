def main():
    
    # NOTE slices use indexes starting at 0 up to 1-length
    # the second index in a slice is "up to but not including"
    # For example: myList[1:3] returns the item at index 1 
    # up to but not including the item at index 3, which is
    # the same as saying the second item and the third item        
    
             #  0      1      2       3        4 
    myList = ['Cat', 'Dog', 'Fish', 'Boat', 'House']    
    print("%s\n" % myList)    
    
    print("myList[1:3] - A slice containing the second up to but not including the fourth")
    print("%s" % myList[1:3])

    print("\nmyList[2:] - A slice containing all items from third to the end")
    print("%s" % myList[2:])

    print("\nmyList[:3] - A slice containing the first item up to but not including the fourth")
    print("%s" % myList[:3])

    print("\nmyList[:] - A slice containing all items")
    print("%s" % myList[:])
    
        #012345678
    s = "something"    
    print("\ns[:4] and s[4:]- You can even use slices on strings!")
    print("%s" % s[:4])
    print("%s" % s[4:])

  
# Call main to kick off the program...  
main()


