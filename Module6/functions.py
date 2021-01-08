def tokenize(line, delimiter):        
    # this variable is used to 'build'
    # a token one character at a time...
    token = ''
    
    # this list is used to hold all of the tokens
    # we find on a line...
    tokens = []
    
    # make sure each line in the file ends with a
    # delimiter, this makes the read of the code simpler...
    if line[len(line)-1] != delimiter: 
        line = line + delimiter
    
    # for each character in the line...
    for char in line:
        # if the current character is a delimiter and the token
        # we have built is not empty...        
        if char == delimiter:
            if token.strip() != '':
                # remove any whitespace from begining and end
                # of token...
                token = token.strip()
            
                # add token to the list...
                tokens.append(token)
            
                # reset the token...
                token = ''
            
        # if the current character is not a delimiter
        # add it to the token we are building...
        else:            
            token = token + char
            
    return tokens
    
def readScores(filename):
    # this list will contain each gamer in the file...
    gamers = []
    
    file = open('scores.txt', 'r')

    for line in file:
        # break the line up into the name and scores...
        tokens = tokenize(line, ',')
        
        # this dictionary will contain the gamer..
        gamer = {}
    
        # add the name to the gamer dictionary...
        gamer['name'] = tokens[0]
        
        # add the scores list to the dictionary...
        gamer['scores'] = tokens[1:]
        
        # append the gamer dictionary to the list of gamers...
        gamers.append(gamer)
    
    file.close()
    
    return gamers
    

        
    