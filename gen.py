import random

play_again = True
total = 0
min = 1

how_many_dice = input("How many dice are you playing with? ")
max = input("How many sides does your dice have? ")

while play_again:
  print()
  values = []

  for y in range(0, int(how_many_dice)):
    values.append(random.randint(min, int(max)))
    print("Dice #" + str(y + 1) + ": " + str(values[y]))

  print()
  for x in range(0, len(values)):
    total += values[x]
  print("Total: " + str(total))
  print()

  choice = input("Do you want to [roll] again, [change] your dice or [stop] rolling? ").lower()
  if choice == "stop rolling" or choice == "stop":
    play_again = False
  elif choice == "change dice" or choice == "change":
    total = 0
    how_many_dice = input("How many dice are you now playing with? ")
    max = input("And those dice have how many sides? ")
    print("Rolling...")
  elif choice == "roll again" or choice == "roll":
    total = 0
    print("Rolling...")
  else:
    print("Sorry, that's not a valid response. Quitting program.")
    play_again = False
