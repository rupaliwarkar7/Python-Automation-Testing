f = open("demofile.txt", "r")
print(f.read())


f = open("demofile.txt", "r")
print(f.read(5))



f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


#import os
#os.remove("demofile.txt")