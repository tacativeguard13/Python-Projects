import os


import os

oldFile = "Sample.txt"
newFileName = input("Enter a file name to rename\n")
newFile = newFileName

with open(oldFile) as old:
    oldread = old.read()

with open(newFile , 'w') as new:
    new.write(oldread)

os.remove(oldFile)