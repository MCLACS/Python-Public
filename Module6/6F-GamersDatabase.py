from functions import readScores

def main():
    
    # read in the gamers...
    gamers = readScores('scores.txt')

    # allow the user to view the gamer's score...
    name = ''
    while name != 'Q':
        name = input("Enter name: (q to quit): ")
        name = name.upper()
        for gamer in gamers:
            if gamer['name'].upper() == name:
                print("Name: %s" % gamer['name'])
                print("Scores: %s" % gamer['scores'])
                print()
        
main()

    




