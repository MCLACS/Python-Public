from functions import tokenize

def main():
    file = open('scores.txt', 'r')

    scores = []
    for line in file:
        list = tokenize(line, ',')
        nums = list[1:]
        for s in nums:
            scores.append(int(s))

    print(max(scores))

    file.close()

main()

    
