print('Welcome to the game!')
name = input('Your name please')
age = int(input('And you age?'))

print('Hello {} of age {}.'.format(name, age))

if age >= 18:
	print('You may pass..')

	wants_to_play = input('Want to play a game? ').lower()
	if wants_to_play == 'yes':
		print("Then let's play")
	else:
		print('Farewell...')
else:
	print('You may not pass.')