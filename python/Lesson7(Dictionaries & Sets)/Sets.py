#SETS(No Duplicate )if your data has then it will ignore it
nums={1,2,3,4}

nums2=set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#it take True and False as 1,0 as well
nums={1,2,2,3,True}
print(nums)

#check ifa value is in a set
print(2 in nums)

#Cannot refer to an element in a set with index

#Add new elements
nums.add(10)
print(nums)

#can use update with lists,tuples,and dictionries
morenums={5,6,7}
nums.update(morenums)
print(nums)

#merge 2 sets to create a new set
one={1,2,3,4}
two={5,6,7,8}

newset=one.union(two)
print(newset)

#keep only duplicates
one={1,2,3,4}
two={3,4,7,8}
print(one.intersection(two))

#will remove all elements from one other than duplicates
one={1,2,3,4}
two={3,4,7,8}
one.intersection_update(two)
print(one)
print(two)

#will store everything except duplicates in one
one={1,2,3,4}
two={3,4,7,8}
one.symmetric_difference_update(two)
print(one)



