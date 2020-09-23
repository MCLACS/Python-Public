num = int(input("Enter a integer: "))

remainder = num % 2

if remainder == 1:
    print("%d is odd" % num)
else:
    print("%d is even" % num)