# Magic Numbers
IN_FT = 12
CM_IN = 2.54

name = input("Eter your name:")

feet = int(input("Enter the feet portion or your height:"))
inches = int(input("Enter the inches portion your height:"))

feet_to_inches = feet * IN_FT
height_in_inches = feet_to_inches + inches

height_in_cm = height_in_inches * CM_IN

print("Hello %s!\n" % name)
print("Your height in centimeters is %.2f" % height_in_cm)