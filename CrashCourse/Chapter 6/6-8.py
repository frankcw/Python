#pets dictionaries within dictionaries


suki={'owner':'frank',
	'kind':'dog',
}

jj={'owner':'claudia',
	'kind':'cat'
}

sparky={'owner':'matteo',
	'kind':'bird'
}

pets=[suki,jj,sparky]


for pet in pets:
	print(pet['owner'].title() +
	' owns a ' + pet['kind'] + '.')