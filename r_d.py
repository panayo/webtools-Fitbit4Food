myList = ['one ', 'six','ten 2']

if any(len(x.split()) > 1 for x in myList):
    print ("Found a match")
else:
    print ("Not a match")
