#Rock Paper Scissors -- attempt 1
# print("Rock...")
# print("Paper...")
# print("Scissors...")

# plr1 = input("player 1, make your choice: ")
# plr2 = input("player 2, make your choice: ")

# if plr1 == "rock" and plr2 == "scissors":
	# print("Player 1 wins!")
# elif plr1 == "rock" and plr2 == "paper":
	# print("Player 2 wins!")
# elif plr1 == "paper" and plr2 == "rock":
	# print("Player 1 wins!")
# elif plr1 == "paper" and plr2 == "scissors":
	# print("Player 2 wins!")
# elif plr1 == "scissors" and plr2 == "paper":
	# print("Player 1 wins!")
# elif plr1 == "scissors" and plr2 == "rock":
	# print("Player 2 wins!")
# elif plr1 == plr2:
	# print("It's a tie!")
# else:
	# print("something went wrong!")



#Rock Paper Scissors -- attempt 2	
# print("Rock...")
# print("Paper...")
# print("Scissors...")

# plr1 = input("Player 1, make your choice: ")
# print("*******NO CHEATING!****\n\n" * 20)
# plr2 = input("Player 2, make your choice: ")

# if plr1 == plr2:
	# print("It's a tie!")
# elif plr1 == "rock":
	# if plr2 == "scissors":
		# print("Player 1 wins!")
	# elif plr2 == "paper":
		# print("Player 2 wins!")
# elif plr1 == "paper":
	# if plr2 == "rock":
		# print("Player 1 wins!")
	# elif plr2 == "scissors":
		# print("Player 2 wins!")
# elif plr1 == "scissors":
	# if plr2 == "paper":
		# print("Player 1 wins!")
	# elif plr2 == "rock":
		# print("Player 2 wins!")
# else:
	# print("something went wrong!")
	

#Rock Paper Scissors -- extra idea...	
# print("Rock...")
# print("Paper...")
# print("Scissors...")

# plr1 = input("Player 1: rock, paper, scissors ")
# print("*******NO CHEATING!****\n\n" * 20)
# plr2 = input("Player 2: rock, paper, scissors ")

# if plr1 == plr2:
	# print("It's a tie!")
# elif p1 == "rock" and p2 == "scissors":
    # print("p1 wins")
# elif p1 == "paper" and p2 == "rock":
    # print("p1 wins")
# elif p1 == "scissors" and p2 == "paper":
    # print("p1 wins")
# else:
    # print("p2 wins")
	
#Rock Paper Scissors --- attempt 3 -- with pseudo AI
from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")
print("")
print("SHOOT!")
print("")
plr = input("Player, make your choice: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer plays {computer}" )
if plr == computer:
	print("It's a tie!")
elif plr == "rock":
	if computer == "scissors":
		print("Player wins!")
	elif computer == "paper":
		print("Computer wins!")
elif plr == "paper":
	if computer == "rock":
		print("Player wins!")
	elif computer == "scissors":
		print("Computer wins!")
elif plr == "scissors":
	if computer == "paper":
		print("Player wins!")
	elif computer == "rock":
		print("Computer wins!")
else:
	print("Please enter a valid choice!")













































