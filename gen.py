import random

min = 1
max = raw_input("How many sides does your dice have? ")
how_many_dice = raw_input("How many dice are you playing with? ")

values = []

for x in range(0, int(how_many_dice)):
  values.append(random.randint(min, int(max)))
  
print values
