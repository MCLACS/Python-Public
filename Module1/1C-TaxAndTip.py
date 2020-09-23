TAX_RATE = 0.05
TIP_RATE = 0.20

# Ask user to enter cost
cost = float(input("Enter cost of meal:"))

# Calc tax and tip
tax = cost * TAX_RATE
tip = cost * TIP_RATE

# Calc total cost
total = cost + tax + tip

# Print the result
print("The tip is $%.2f\nThe tax is $%.2f\n\nThe total is $%.2f" % \
      (tip, tax, total) )

