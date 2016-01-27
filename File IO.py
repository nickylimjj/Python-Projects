import os

f = open('hello.txt','wb') #created in same dir

# ---file modes---
# r: read only;
# r+: read and write
# w:Opens a file for writing only.
#     Overwrites the file if the file exists.
#     If the file does not exist,
#     creates a new file for writing.
# w+: read and write
# a: appending. File pointer is at the end of the file if the file exists. 
#     That is, the file is in the append mode. 
#     If the file does not exist, it creates a new file for writing.
# a+: read and append.
# ---file modes---

print "Name of the file: ", f.name
print "Closed or not : ", f.closed
print "Opening mode : ", f.mode
print "Softspace flag : ", f.softspace

f.write('learning to write!')
f.close()

with open('hello.txt','r+') as f:
    print '\n' + f.read()

os.rename('hello.txt','renamed.txt')
os.remove('renamed.txt')