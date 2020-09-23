vowels = 0
word = input("Enter a word: \n")
word = word.upper()

for ch in word:
    if ch == 'A' or ch == 'E' or \
       ch == 'I' or ch == 'O' or \
       ch == 'U' or ch == 'Y':
        vowels = vowels + 1
        
print ("%s has %d letters and %d are vowels." % ( word, len(word), vowels))