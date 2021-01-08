# create a dictionary...
person = {'first': 'Devon', 'last': 'Sterling'}

# print the keys, note these are stored in a regular python list...
print("Keys: %s\n" % person.keys())

# print the values, note these are stored in a regular python list...
print("Values: %s\n" % person.values())

# access values using the keys...
print("Full Name: %s, %s\n" % (person['last'], person['first']))

# edit a value...
person['last'] = 'Rodgers'
print("Full Name: %s, %s\n" % (person['last'], person['first']))

# add a new key/value pair...
person['age'] = 19
print("Keys: %s" % person.keys()) 
print("Values: %s" % person.values())
print("Full Name: %s, %s, %d years old\n" % (person['last'], person['first'], person['age']))

print(person)

    

