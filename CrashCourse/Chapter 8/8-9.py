#function with a list

magician_names = ['magicarp','mr. mime','abra']

def show_magicians(magician):
	for magician in magician_names:
		print(magician.title())

name = show_magicians
name(magician_names)