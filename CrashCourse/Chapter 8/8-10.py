#8-10. Great Magicians: Start with a copy of your program from Exercise 8-9



#function with a list, modifying it

magician_names = ['magicarp','mr. mime','abra']
temp_list = []


def show_magicians(magician):
	for magician in magician_names:
		print(magician.title())

def make_great(great):
	while magician_names:
		new_name = magician_names.pop()
		complete_name = "The Great " + new_name.title()
		temp_list.append(complete_name)
	print (temp_list)
	magician_names.append(temp_list)


name = show_magicians
name(magician_names)

print('\n')

completed_names = make_great
completed_names(magician_names)
