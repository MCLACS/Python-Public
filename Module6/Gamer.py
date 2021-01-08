from functions import readScores

def main():
    
    gamers = readScores('scores.txt')

    choice = ''
    while choice != 'Q':
        found = False
        deleted = False
        print()
        print("What would you like to do?")
        print("V - View a specific gamer")
        print("E - Edit a gamer's name")
        print("D - Delete a gamer")
        print("Q - Quit")
        choice = input().upper()
        if choice == 'V':            
            name = input("Enter gamer's name: ").upper()
            for gamer in gamers:
                if gamer['name'].upper() == name:
                    print("Name: %s" % gamer['name'])
                    print("Scores: %s" % gamer['scores'])
                    print()
                    found = True
            if found == False:
                print("Gamer not found!")
        elif choice == 'E':            
            name = input("Enter gamer's name: ").upper()
            for gamer in gamers:
                if gamer['name'].upper() == name:
                    gamer['name'] = input("Enter new name: ")
                    print("Name changed")
                    found = True
            if found == False:
                print("Gamer not found!")
        elif choice == 'D':            
            name = input("Enter gamer's name: ").upper()
            for i in range(0, len(gamers)):
                if deleted == False and gamers[i]['name'].upper() == name:
                    gamers.pop(i)
                    print("Gamer deleted")
                    found = True
                    deleted = True
            if found == False:
                print("Gamer not found!")                
        elif choice != 'Q':
            print("Invalid option")
            
    print('Bye')
                
main()
