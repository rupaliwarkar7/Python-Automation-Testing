try:
  print(x)
except:

  print("An exception occurred")




x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")




#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Rup Something went wrong when opening the file")



  try:
      k = 5 // 0
      print(k)

  except ZeroDivisionError:
      print("Rupali Can't divide by zero")

  finally:
      print('Rupali This is always executed')


