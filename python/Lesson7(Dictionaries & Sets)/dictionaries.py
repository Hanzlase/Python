#Dictionaries save data values in key value pair like Hash in java and C++
band={
    "vocals":"Plant",
    "guitar":"page",
}

band2=dict(vocals="plants",guitar="page")

print(band)
print(band2)

print(type(band))
print(len(band))

#Acess items
print(band["vocals"])
print(band.get("guitar"))

#List all keys
print(band.keys())

#list all values
print(band.values())

#List key/value pairs
print(band.items())

#veify key existence
print("guitar" in band)
print("tri" in band)

#Change/Add values
band["values"]="Coverdale"
band.update({"bass":"JPJ"})
print(band)

print(band.pop("bass"))

band["drums"]="Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

#delete and clear
band["drums"]="Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#Copy Dictionaries
# (Dont)
band2=band #create a refrence
print("Bad copy")
print(band)
print(band2)

#Adding/Removing in 1 will add in both
# band2["drums"]="Dave"
# print(band)

#DO
band2=band.copy()
band2["drums"]="Dave"
print("Good copy")
print(band)
print(band2)

#copy using constructor function
band3=dict(band2)
print("Good copy")
print(band3)

#Nested Dictionaries
s1={
    "name":"Hanzla",
    "Degree":"SE"
}
s2={
    "name":"Saad",
    "Degree":"CS"
}
s3={
    "name":"Ali",
    "Degree":"AI"
}
students={
    "Student1":s1,
    "Student2":s2,
    "Student3":s3
    
}
print(students)
#print the name of student 1
print(students["Student1"]["name"])

