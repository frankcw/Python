#function with a list, create a list with a copy and show both with a function


def show_magicians(show_list):
	for magician in show_list:
		print(magician.title())

def make_great(magician_names):
	while magician_names:
		new_name = magician_names.pop()
		complete_name = "The Great " + new_name.title()
		temp_list.append(complete_name)
	
		
		
magician_names = ['magicarp','mr. mime','abra']
temp_list = []


make_great(magician_names[:])
show_magicians(magician_names)
show_magicians(temp_list)

	