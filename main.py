import random

#List of results and moves to keep track of all winning combinations
results = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"), ("rock", "lizard"), ("lizard", "spock"), ("spock", "scissors"), ("scissors", "lizard"), ("lizard", "paper"), ("paper", "spock"), ("spock", "rock")]
#What the computer will choose (takes the first element of each tuple)
moves = [result[1] for result in results]

#Keeps track of the score
player_one_score, cpu_score = (0, 0)

#Asks the player what object they want to be
player_one = input("Enter rock/paper/scissors/lizard/spock/quit: ").lower()
cpu = random.choice(moves)

#Keeps doing this until the user quits
while player_one != "quit":
  #Plays the game
  cpu = random.choice(moves)
  print("You chose {}, I chose {}".format(player_one, cpu))
  #Determines who wins and loses
  if player_one == cpu: #when you choose same object as computer
    print("It's a tie!")
  elif (player_one, cpu) in results: #When you choose a dominant object over the computer
    print("You win!")
    player_one_score += 1
  elif (cpu, player_one) in results: #When computer choose a dominant object over you
    print("You lose!")
    cpu_score += 1
  else:
    print("You did not choose a valid option, please choose a correct option!")
  player_one = input("Enter rock/paper/scissors/lizard/spock/quit: ").lower()
#Once player quits, the score will be displayed
print("FINAL SCORES")
print("You {}, Me {}".format(player_one_score, cpu_score))
if player_one_score > cpu_score:
  print("Yay, congratulations!!!")
else:
  print("Oh no, keep on trying. I am sure you will win one day :)")
