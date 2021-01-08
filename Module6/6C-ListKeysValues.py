# create a list...
person = ['Devon', 'Sterling']

# print the keys...
print("Keys: ", end = '')
print(*range(0, len(person)))
      
#print the values...
print("Values: %s\n" % person)

# access values using the keys...
print("Full Name: %s, %s\n" % (person[1], person[0]))

# edit a value...
person[1] = 'Rodgers'
print("Full Name: %s, %s\n" % (person[1], person[0]))

# add a new key/value pair for age...
person.append(19)
print("Keys: ", end = '')
print(*range(0, len(person)))
print("Values: %s" % person)
print("Full Name: %s, %s, %d years old\n" % (person[1], person[0], person[2]))


    

