rows = int(input("Enter the number of rows: \n"))

print("%4s %4s %4s" % ("----","----","----"))
print("%4s %4s %4s" % ("Col0","Col1","Col2"))
print("%4s %4s %4s" % ("----","----","----"))

for row in range(0,rows):
    for col in range(0,3):
        print("%4d " % col, end = "")
    print()
