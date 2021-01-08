from functions import readScores

def main():
    
    gamers = readScores('scores.txt')
    print(gamers[1]['scores'][0])

main()

    



