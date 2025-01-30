#Tuples cannot be changed
mytuple=tuple(("Hanzla",23,True))
print(mytuple)

mytuple2=("Hanzla",23,True)
print(mytuple2)

newlist=list(mytuple2)
newlist.append(1)
print(newlist)