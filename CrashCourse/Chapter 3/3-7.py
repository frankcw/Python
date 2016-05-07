#Guest list with message with pop variable and loop message

guests=['matt','syedur','phil']

leaving_guest=guests.pop(0)

print(leaving_guest.title()+" wont be able to make it\n")

guests.append('jimmy')

for guest in guests:
    print('Hello '+guest.title()+', you are invited to dinner at my house\n')
    
print('I was able to find a bigger table\n')

guests.insert(0,'tommy')
guests.insert(2,'john')
guests.append('frank')


for guest in guests:
    print('Hello '+guest.title()+', you are invited to dinner at a new place I found\n\n')
 
leaving_guests=[]
leaving_guests.append(guests.pop())
leaving_guests.append(guests.pop())
leaving_guests.append(guests.pop())

for leaving_guest3 in leaving_guests:
    print('I wont be able to invite you anymore '+  leaving_guest3.title())  
