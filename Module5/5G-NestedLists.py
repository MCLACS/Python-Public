def main():

    # initial student database...
    students = [ ["Sophia", 88, 75, 92], \
                 ["Rafael", 72, 69, 88], \
                 ["Isabella", 93, 98, 86] ]
    students.sort()

    # print database...
    print()
    for student in students:
        print(student)
    print()    

    # add new students...
    name = ""
    while name != "q":
        name = input("New student's name (q to quit): ")
        if name != "q":
            g1 = int(input("First grade: "))
            g2 = int(input("Second grade: "))
            g3 = int(input("Third grade: "))
            student = [name, g1, g2, g3]
            students.append(student)
    students.sort()

    # print database...
    print()
    for student in students:
        print(student)
    print()    

    # lookup students...
    name = ""
    while name != "q":
        name = input("Lookup student's grades (q to quit): ")
        if name != "q":
            for student in students:
                if student[0].upper() == name.upper():
                    print("%s has the following grades %s: " % (name, student[1:]))
                    
# kickoff the main program
main()
