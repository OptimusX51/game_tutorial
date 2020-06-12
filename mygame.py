print('Welcome to the game!')
name = input('Your name please: ')
age = int(input('And you age? '))

hp = 10

if age >= 18:
	print('You may pass..')

	wants_to_play = input('Want to play a game? ').lower()
	if wants_to_play == 'yes':
		print("Then let's play")
		print('Hello {} of age {}.  You have {} health.'.format(name, age, hp))

		left_or_right = input('We begin...which direction do we go?\n(left or right?)').lower()
		if left_or_right == 'left':
			ans = input('You come upon a lake... Do you swim across or go around?/(swim/around)').lower()
			if ans == 'around':
				print('You walk around the lake and come upon a house.')
			elif ans == 'swim':
				print('You see a mermaid as you swim across.  She bids you follow her and you do.  You swim after her down, down, down.')
				while True:
					hp -= 5
					print('hp -5\nremaining hp = {}'.format(hp))
					ans = input('Swim back to the surface or continue to follow?\n(up/down)')
					if ans == 'down':
						continue
					else:
						break
				print('You swim back to the surface and make it to shore')
				ans = input('You are at a delta.  There\'s a house nearby.  Do you go up the river or to the house?\n(river/house)')
				if ans == 'house':
					print('You go to the house.  A crazed man comes out running at you and bites you.  You manage to get him off and knock him out, but lose 5 hp.')
					hp -= 5
					print('Your hp is now at {} hp.'.format(hp))
					if hp <= 0:
						print('You are out of hp.  You have perished.  Game Over')
				else:
					print('The mermaid was waiting for you in ambush.  She grabs you by the arm and pulls you underwater...')
			else:
				print('Poor choice...')
		else:
			print('You walked into a spider\'s web never to be seen again...')

	else:
		print('Farewell...')
else:
	print('You may not pass.')
