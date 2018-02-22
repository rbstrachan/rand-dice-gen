import random

play_again = True

min = 1

while play_again:
	max = raw_input("How many sides does your dice have? ")
	how_many_dice = raw_input("How many dice are you playing with? ")

	values = []

	for x in range(0, int(how_many_dice)):
		values.append(random.randint(min, int(max)))
  
	print
  
	for x in values:
		print x

	print

	again = raw_input("Do you want to roll again? ")
	if again.lower() == "no" or again.lower() == "n":
		play_again = False
	else:
		print
