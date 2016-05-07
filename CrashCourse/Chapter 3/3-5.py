#Guest list with message and pop

guests=['matt','syedur','phil']

leaving_guest=guests.pop(0)

print(leaving_guest.title()+" wont be able to make it\n")

guests.append('jimmy')

for guest in guests:
    print('Hello '+guest.title()+', you are invited to dinner at my house\n')