txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)


txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)




txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)



txt = " banana  "
x = txt.strip()
print("In all fruits", x, "is my favorite")


#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


txt = "welcome to the jungle"
x = txt.split()
print(x)

a = "Hello"
# Slices the string from 0 to 3 indexes
print(a[0:3])
# Slices the string from 3 to -1(same as 4) indexes
print(a[3:-1])