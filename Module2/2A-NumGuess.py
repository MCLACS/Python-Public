from random import randrange

START = 1
END = 10

ans = randrange(START,END+1)

guess = int(input('Pick a number from %d to %d: ' % (START, END)))

if (guess == ans):
    print("You win!")
else:
    print("You loose!")