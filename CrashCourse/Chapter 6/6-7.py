#people nesting 

people={
		'user_1':{
			'first':'frank',
			'last':'cordova',
			'age':'26',
			'location':'new york'
			},
		'user_2':{
			'first':'claudia',
			'last':'rivadeneira',
			'age':'26',
			'location':'bound brook',
			},
		'user_3':{
			'first':'jorge',
			'last':'contreras',
			'age':'30',
			'location':'guayaquil',
			}
	
		}


for user in people:
	print(user['first'].title() + user['last'].title() + 
		' lives in ' + user['location'].title() + 
		' and is ' + user['age'])
