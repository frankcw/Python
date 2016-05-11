#favorite places dictionary

favorite_places={
	'person1':{
		'name':'frank',
		'place1':'ecuador',
		'place2':'london' 
	},
	'person2':{
		'name':'claudia',
		'place1':'ecuador',
		'place2':'paris',
	},
	'person3':{
		'name':'robert',
		'place1':'united states',
		'place2':'egypt',
	},
}

for key,person in favorite_places.items():
	print(person['name'].title() + 
		"'s favorite places are " +
		person['place1'].title() + ' and ' +
		person['place2'].title() + '.')