# Python program to demonstrate
# logical and operator
a = 10
b = 10
c = -10
if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

# 2nd PROGRAM
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

# 3rd PROGRAM
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

# Python program to demonstrate
# logical not operator
a = 10

if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")