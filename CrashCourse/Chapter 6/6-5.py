#rivers and countries with dictionaries

rivers = {
	'nile':"egypt",
	'guayas':'ecuador',
	'hudson':'united states',
	'amazonas':'brazil',
	}

for k , v in rivers.items():
	print('The ' + k.title() + ' river runs in ' + v.title()  + '.')

    