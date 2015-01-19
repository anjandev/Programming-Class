# Problem S2: Assigning Partners 
# Senior Division

numberofkids = int(input("Enter the number of kids in the class"))

names1 = input("Enter the names of kids in the class")
names1 = names1.split()

names2 = input("Enter the names of kids in the class (second entry)")
names2 = names2.split()

partnersdict = {}
partnersdict2 = {}

for name in range(len(names1)):
    partnersdict[names1[name]] = names2[name]
    
for name in range(len(names2)):
    partnersdict2[names2[name]] = names1[name]

goodorbad = "good"
    
for names in names1:
    if partnersdict2[names] != partnersdict[names]:
        goodorbad = "bad"
        break

print goodorbad
