month = str.upper(input("Enter a month:"))
days = 31

if  (month == 'SEPTEMBER') or (month == 'APRIL') or \
    (month == 'JUNE') or (month == 'NOVEMBER'):
    days = 30
    print("Case 1")
elif month == 'FEBRUARY':
    days = '28 or 29'
    print("Case 2")
else:
    days = 31
    print("Case 3")
    
print("%s has %s days" % (month, days))

    