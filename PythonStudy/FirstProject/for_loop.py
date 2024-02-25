fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["peru", "melon", "cherry"]
for x in fruits:
    if x == "peru":
        break
    print(x)

# While loop
#With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i +=1

#With the continue statement we can stop the current iteration, and continue with the next:
  i = 0
  while i < 8:
      i += 1
      if i == 4:
          continue
      print(i)


#the pass statement
def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement

a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement
