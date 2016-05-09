#confitional tests

state="NJ"

print(state=='NJ')

print(state=='nj')

#using lower()
print(state.lower()=="nj")

print("\n\n")


#numerical conditionals
age_0=18
age_1=21


print(age_0 >= 18)
print(age_0 >= 21)


print(age_0 >= 21 or age_1 >= 21)


#whether an item is on a list or not

pizza_ingredient=['honey','mushroom','ham']
special_ingredient='ham'
hated_ingredient='ollives'


if special_ingredient in pizza_ingredient:
	print(special_ingredient.title()+' is in the pizza')

if hated_ingredient not in pizza_ingredient:
	print(hated_ingredient.title()+' are not in the pizza')
