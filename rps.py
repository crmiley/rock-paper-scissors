import random

player_wins = 0
computer_wins = 0

while (player_wins + computer_wins < 3):

	print("Welcome to Rock, Paper, Scissors!")
	 
	player_choice = raw_input("Rock, Paper, or Scissors?")

	computer = random.randint(1,4)

	#int 1 = "Rock"
	#int 2 = "Paper"
	#int 3 = "Scissors"

	computer_choice = 0
	if computer == 1 and player_choice == "paper":
		print("USER WINS")
		player_wins = player_wins + 1
	elif computer == 2 and player_choice == "paper":
		print("TIE GAME")
	elif computer == 3 and player_choice == "paper":
		print("Computer Wins")
		computer_wins = computer_wins + 1
	elif computer == 1 and player_choice == "rock":
		print("TIE GAME")
	elif computer == 2 and player_choice == "rock":
		print("Computer Wins")
		computer_wins = computer_wins + 1
	elif computer == 3 and player_choice == "rock":
		print("USER WINS")
		player_wins = player_wins + 1
	elif computer == 1 and player_choice == "scissors":
		print("Computer Wins")
		computer_wins = computer_wins + 1
	elif computer == 2 and player_choice == "scissors":
		print("USER WINS")
		player_wins = player_wins + 1
	elif computer == 3 and player_choice == "scissors":
		print("TIE GAME")
	else: 
		print("Error")
 

	