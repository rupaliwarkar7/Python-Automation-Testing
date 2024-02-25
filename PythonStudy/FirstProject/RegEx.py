import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())



#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

  # Return a list containing every occurrence of "ai":


