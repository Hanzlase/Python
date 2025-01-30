#While loop
value=1
while value<10:
    print(value)
    value+=1
    
#Using break
print("") 
value=1
while value<=10:
    print(value)
    if(value==5):
        break
    value=value+1
 
#For loop
names=["Hanzla","Saad","Ali","Abdullah"]
for x in names:
    print(x)

#print each alphabet
for x in"Mississippi":
    print(x)
    
for x in names:
    if x=="Hanzla":
        print(x)
        break

#Will print everyname except Hanzla
print("")
for x in names:
    if x=="Hanzla":
        continue
    print(x)

#before 4
print("")
for x in range(4):
    print(x)
    
#from 2 to 9
print("")
for x in range(2,10):
    print(x)
    

#will increment by 5
print("")
for x in range(0,100,5):
    print(x)
else:
    print("Glad That's Over")

names=["Hanzla","Saad","Abdullah"]
actions=["eats","codes","sleeps"]

#nested loops
print("")
for name in names:
    for action in actions:
        print(name +" "+action+".")
        
