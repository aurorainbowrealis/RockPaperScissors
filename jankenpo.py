import numpy as np

#returns a number from 1 to 3
def get_computer_play():
	return np.random.randint(1,4)

#gets the player and computer play and apply rock, paper scissors rules
#returns
#0 - Draw
#1 - Player
#2 - Computer
def get_winner(player, computer):
	if player == computer:
		return 0
	#rock x scissors
	elif (player == 1 and computer == 3):
		return 1
	elif (player == 3 and computer == 1):
		return 2
	elif player > computer:
		return 1
	return 2

def result(winner):
	res = ['Tie', 'Player wins', 'Computer wins']
	return res[winner]

def main():
	print('Welcome to Rock, Paper and Scissors!')
	is_playing = True
	while is_playing:
		is_right = False
		plays = ['Rock', 'Paper', 'Scissors']
		while not is_right:
			player = input('What is your input?\n1 - Rock, 2 - Paper, 3 - Scissors\n')
			try:
				player = int(player)
				if player in [1,2,3]:
					is_right = True
				else:
					print('Invalid Input')
			except:
				print('Invalid Input')

		computer = get_computer_play()
		print('Player shows {}, computer shows {}'.format(plays[player - 1], plays[computer - 1]))
		print(result(get_winner(player, computer)))

		play_again = input('Would you like to play again? (Y/y for YES, anything else for NO)').upper()
		if play_again != 'Y':
			is_playing = False


if __name__ == '__main__':
	main()