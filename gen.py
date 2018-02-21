import random

how_many_dice = raw_input("How many dice are you playing with? ")
values = []

for x in range(0, int(how_many_dice)):
  values.append(random.randint(1,6))
  
print values
