#if statements

alien_color=['green','yellow','red']

if 'green' in alien_color:
	print('You just earned 5 points')

#another version where it fails all colors and there is no output

for color in alien_color:
	if color is 'blue':
		print("This color doesn't really exist so there should be no output")