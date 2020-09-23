# Containers <= 1 liter $0.10 deposit
SMALL_DEPOSIT = 0.10

# Containers > 1 liter $0.25 deposit
LARGE_DEPOSIT = 0.25

small = int(input("Enter the number of small containers:"));
large = int(input("Enter the number of large containers:"));

refund = (small * SMALL_DEPOSIT) + (large * LARGE_DEPOSIT)

print('Your refund is $%.2f' % refund)
