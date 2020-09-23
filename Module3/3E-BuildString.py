start = input("Enter starting letter: \n")
startLen = int(input("Enter number of starting letters: \n"))

mid = input("Enter middle letter: \n")
midLen = int(input("Enter number of middle letters: \n"))

end = input("Enter ending letter: \n")
endLen = int(input("Enter number of ending letters: \n"))

s = ""

for i in range(0, startLen):
    s = s + start.lower() 

for i in range(0, midLen):
    s = s + mid.upper() 

for i in range(0, endLen):
    s = s + end.lower()
    
print(s)

