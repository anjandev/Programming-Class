# Problem S1: Party Invitation. For Waterloo Computing Competition. 
# Senior Division

numfriends = int(input("Enter the number of friends to invite"))
numsforfriends = []

for x in range(1,(numfriends + 1)):
    numsforfriends.append(x)
    
roundremove = int(input("Enter the number of rounds of removal"))

removepositions = []

for y in range(roundremove):
    removeposition = int(input("Enter positions to remove"))
    removepositions.append(removeposition)

for removenum in removepositions:
    delitirations = len(numsforfriends) // removenum
    posinlist = 0
    for g in range(1, delitirations + 1):
        posinlist = posinlist + removenum - 1
        numsforfriends.pop(posinlist)
        
for survivedfriends in numsforfriends:
    print survivedfriends
