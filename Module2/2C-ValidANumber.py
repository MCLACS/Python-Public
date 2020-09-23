anum = str.upper(input("Enter your A Number: "))
valid = True

if len(anum) != 9:
    valid = False
elif anum[0] != 'A':
    valid = False
elif anum[1].isdigit() == False:
    valid = False
elif anum[2].isdigit() == False:
    valid = False
elif anum[3].isdigit() == False:
    valid = False
elif anum[4].isdigit() == False:
    valid = False
elif anum[5].isdigit() == False:
    valid = False
elif anum[6].isdigit() == False:
    valid = False
elif anum[7].isdigit() == False:
    valid = False
elif anum[8].isdigit() == False:
    valid = False
else:
    valid = True
    
if valid:
    print("'%s' is a valid A number" % anum)
else:
    print ("'%s' is not a valid A number" % anum)