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

def readTemps(file):
    temps = []
    f = open(file, 'r')
    for line in f:
        tokens = tokenize(line, ',')
        temps.append( {'high': int(tokens[0]), 'low': int(tokens[1])} )
    return temps

def getAverages(temps):
    ave = []
    for t in temps:
        a = (t['high']+t['low'])/2.0
        ave.append(a)
    return ave

def countHotCold(temps):
    hot = 0
    cold = 0
    for t in temps:
        if t['high'] >= 70:
            hot = hot + 1
        elif t['low'] <= 50:
            cold = cold + 1             
    return {'hot': hot, 'cold': cold}
        