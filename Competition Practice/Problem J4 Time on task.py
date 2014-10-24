# This program solves problem 4: Time on Task

chore_times = 0

t = int(input("What is the total number of minutes I have available to complete my chores"))
c = int(input("What is the total number of chores that you may choose from"))

for i in range(c):
    chore_times += int(input("How long does this chore take?"))

complete = chore_times // t

print "The total number of chores you can complete in", t, "minutes is", complete,