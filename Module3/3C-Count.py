end = int(input("How far do you want to count? \n"))

print("Counting...")
for i in range(1,end+1):
    print(i, end = " ")

print("")
print("Counting every other number...")
    
for i in range(1,end+1, 2):
    print(i, end = " ")
    
print("")
print("Counting backwards...")
    
for i in range(end, 0, -1):
    print(i, end = " ")
    
print("")
print("Counting every other backwards...")
    
for i in range(end, 0, -2):
    print(i, end = " ")            