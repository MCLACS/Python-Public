#############################################
# popluates a list with numbers entered by
# the user
#############################################
def populateListFromUser(myList):
    num = 0
    while (num != -1):
        num = int(input("Enter a number (-1 to quit): \n"))
        if (num != -1):
            myList.append(num)
    return

#############################################
# popluates a list with numbers entered by
# the user but ignores duplicates
#############################################
def populateListFromUserNoDups(myList):
    num = 0
    while (num != -1):
        num = int(input("Enter a number (-1 to quit): \n"))
        if (num != -1 and num not in myList):
            myList.append(num)
    return

#############################################
# converts a string to a list of characers
#############################################
def stringToList(s):
    l = []
    for c in s:
        l.append(c)
    return l

#############################################
# converts a list to a string of characers
#############################################
def listToString(l):
    s = ''
    for item in l:
        s = s + str(item)
    return s
