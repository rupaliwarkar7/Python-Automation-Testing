#Tuple items are ordered, unchangeable, and allow duplicate values.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets  Constructor
print(thistuple)



thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])