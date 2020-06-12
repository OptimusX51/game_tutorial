print('Welcome to the game!')
name = input('Your name please')
age = int(input('And you age?'))

hp = 10

print('Hello {} of age {}.'.format(name, age))

if age >= 18:
	print('You may pass..')

	wants_to_play = input('Want to play a game? ').lower()
	if wants_to_play == 'yes':
		print("Then let's play")

		left_or_right = input('We begin...which direction do we go?\n(left or right?)').lower()
		if left_or_right == 'left':
			ans = input('You come upon a lake... Do you swim across or go around?/(swim/around)').lower()
			if and == 'around':
				print()
			else:
				print('You see a mermaid as you swim across.  She bids you follow her and you do.  You swim down, down, down, until you run out of breath.')

		else:
			print('You walked into a spider\'s web never to be seen again...')

	else:
		print('Farewell...')
else:
	print('You may not pass.')