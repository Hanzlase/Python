users=['Hanzla','Sara',"Charles"]
data=['Hanzla',40,True]
emptylist=[]

print("Hanzla" in users)
print("Hanzla" in emptylist)
print(users[0])
#-1 gives last ,-2 second last
print(users[-1])

print(users.index("Charles"))

#It will exclude 2
print(users[0:2])
print(users[0:3])
print(users[2:])
print(users[-3:-1])

#Length of List
print(len(data))

#add at end
users.append('Elsa')
print(users)

users+=['Jason','Saad']
print(users)

users+='hanzla'
print(users)

users.extend(['Robert','Jimmy'])
print(users)

# users.extend(data)
# print(users)

data.insert(0,"Bob")
print(data)

data[2:2]=['Eddie',32]
print(data)

data[1:3]=['Robert','Khabib']
print(data)

data.remove('Bob')
print(data)

print(data.pop())
print(data)

del data[0]
print(data)

data.clear()
print(data)

users.sort()
print(users)

#will ignore upper,lower case
users.sort(key=str.lower)
print(users)

nums=[2,3,4,12,42,53]
nums.reverse()
print(nums)

#will chnage original list
nums.sort(reverse=True)
print(nums)
nums.sort()
print(nums)
#will not change original list
print(sorted(nums,reverse=True))

#creating copies
numscopy=nums.copy()
mynums=list(nums)
mycopy=nums[:]
print(numscopy)
mynums.reverse()
print(mynums)
print(mycopy)
print(nums)

print(type(nums))

