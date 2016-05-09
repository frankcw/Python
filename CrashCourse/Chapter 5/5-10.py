#list verification/comparison

current_list=['admin','fracor','juaher','matcor']
new_users=['admin','juaher','clariv','britam']

#looping through lists to make sure they dont rerpeat
for new_user in new_users:
	if new_user in current_list:
		print(new_user+" is already a taken username, please change it.")
	else:
		print(new_user+' is an available username.')


