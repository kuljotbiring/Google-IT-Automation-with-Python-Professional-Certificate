# this program checks whether something is a directory or a file
import os

os.listdir("website")
directory = "website"
for name in os.listdir(directory):
    fullname = os.path.join(directory, name)
    if os.path.isdir(fullname):
        print("{} is a directory". format(fullname))
        
    else:
        print("{} is a file".format(fullname))
