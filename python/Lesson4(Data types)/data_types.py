
import math
#String
#literal assignment
first='Hanzla'
last='Sabir'
#will give datatype of first
print(type(first))
print(type(first)==str)
print(isinstance(first,str))

# constructor function
pizza=str("pepporoni")
print(type(pizza))
print(type(pizza)==str)
print(isinstance(pizza,str))

#Cancatenation
fullname=first+" "+last
print(fullname)

# Casting number to String
decade=str(1800)
print(type(decade))
print(decade)

statement="I like rock music from the "+decade+"s."
print(statement)

#Multiple lines
multiline='''
Hey ,how are you
I was just checking in.
All good?
'''
print(multiline)

#Escaping special characters
sentence='I\'m back at University!\t\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

#capital every word 1st letter
print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline+="                                             "
print(len(multiline))
multiline="                         "+multiline
print(len(multiline))

print('\n')
#it remove all empty space
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

#Build a Menu
title="menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".")+"$1".rjust(4))
print("Muffin".ljust(16,".")+"$2".rjust(4))
print("Cake".ljust(16,".")+"$4".rjust(4))
print("")

#String index values
print(first[1])
print(first[-1]) #last letter if first
print(first[0:-1])
print(first[0:])
print("")
#some method return boolean data
print(first.startswith("D"))
print(first.startswith("H"))
print(first.endswith("a"))


#Boolean datatype
myval=False
x=bool(True)
print(type(x))
print(isinstance(myval,bool))

#Numeric data types
#integer 
price=100
best_price=int(80)
print(type(price))
print(isinstance(best_price,int))

#float
gpa=3.28
y=float(1.9)
print(type(gpa))
print("")
#complex type
comp_val=5+3j
print(type(comp_val))
print(comp_val.real) #will give real part
print(comp_val.imag) #will give imaginary part
print("")
#Built in functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa,1))
print("")

#Math functions
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print(" ")

#Casting a String to a number
zipcode="100001"
zip_val=int(zipcode)
print(type(zip_val))