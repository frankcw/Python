#glossary program with loops

glossary = {
	'string': 'text',
	'integer' : 'numbers',
	'methods' : 'used to modify a variable',
	'lists' : 'to list objects',
}

for word,meaning in glossary.items():
	print(word + '\n' + meaning  + '\n')