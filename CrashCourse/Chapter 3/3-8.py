#list of places with sort and reverse


#original list
places=['paris','guayaquil','london','madrid','milan']
print(places)

#temp sort
sorted(places)
print(places)

#reverse permanent list
places.reverse()
print(places)

#reverse permanent list, back to original
places.reverse()
print(places)

#permenent sort in alphabeitcal
places.sort()
print(places)

#permament reverse sort in alphabetical order
places.sort(reverse=True)
print(places)