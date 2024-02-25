#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)





set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)




myset = {"apple", "banana", "cherry"}
print(type(myset))




thisset = {"apple", "banana", "cherry"}
thisset.add("grapes")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)



thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)



set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)



set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)