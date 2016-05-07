#Guest list with message insert and append methods

guests=['matt','syedur','phil']

leaving_guest=guests.pop(0)

print(leaving_guest.title()+" wont be able to make it\n")

guests.append('jimmy')

for guest in guests:
    print('Hello '+guest.title()+', you are invited to dinner at my house\n')
    
print('I was able to find a bigger table\n')

guests.insert(0,'Tommy')
guests.insert(2,'John')
guests.append('frank')


for guest in guests:
    print('Hello '+guest.title()+', you are invited to dinner at a new place I found\n')