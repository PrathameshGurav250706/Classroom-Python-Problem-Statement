# Display city name those are having temperature less than 25degree

s={'Kolhapur':23,'gadhinglaj':29,'pune':10,'mumbai':21}


# d=filter(lambda s:print(s.keys()) if s.values()<25 else False,s.items())
# print(list(d))

d=filter(lambda x: print(x) if s[x]<25 else False,s)
print(list(d))

#--------------------
# a=filter(lambda city:print(city) if s[city]<25 else False,s)
# print(list(a))
