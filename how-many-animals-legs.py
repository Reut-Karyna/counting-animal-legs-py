cows1 = input("How many cows do you have?: ")
chickens1 = input("How many chickens do you have?: ")
pigs1 = input("How many pigs do you have?: ")
cows = int(cows1)
chickens = int(chickens1)
pigs = int(pigs1)

cows_legs = (cows * 4)
pigs_legs = (pigs * 4)
chickens_legs = (chickens * 2)

print ("You have {} animals legs in a farm.".format(cows_legs + pigs_legs + chickens_legs))
