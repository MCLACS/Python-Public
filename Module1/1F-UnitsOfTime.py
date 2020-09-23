# Magic numbers
HR_DAY = 24
MIN_HR = 60
SEC_MIN = 60

days = int(input("Enter days:"))
hours = int(input("Enter hours:"))
mins = int(input("Enter minutes:"))
seconds = int(input("Enter seconds:"))

interval1 = days * HR_DAY * MIN_HR * SEC_MIN
interval2 = hours * MIN_HR * SEC_MIN
interval3 = mins * SEC_MIN

total = interval1 + interval2 + interval3 + seconds

print("Total seconds is %d" % total)


