letter = str.upper(input("Enter a letter:"))
if (letter == 'A') or \
   (letter == 'E') or \
   (letter == 'I') or \
   (letter == 'O') or \
   (letter == 'U'):
    print ('%s is a vowel' % letter)
elif letter == 'Y':
    print ('%s can be either' % letter)
else:
    print ('%s is a consonent' % letter)
