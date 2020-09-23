offer = 0
maxOffer = 0

while (offer != -1):
    offer = int(input("Enter an offer: (enter -1 to quit): \n"))
    if offer > maxOffer:
        maxOffer = offer
        
print("The largest offer is %d. \n" % maxOffer)
        