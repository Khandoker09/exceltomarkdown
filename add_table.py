#######################################################################
#This file will add new sidebar 
# Parameter
#a= """<li><a href="{{ site.baseurl }}/new name">New name</a></li>"""
#write new name in the place of new name without extention 
#######################################################################






#reading header file and save them in a data variable 
myfile = open(r"C:\Users\USER\Desktop\wiki.txt","r+")
data = ""
lines = myfile.readlines()
for line in lines:
    data = data + line.lstrip(" \n ")
    print(data)

#reading header file and save them in a data variable 




file = open(r"F:\1jobsSMO\SMO\SMO-Wiki\_pages\Facebook Tools.md", "r+")
f=file

lines = f.readlines()
print(lines)
for i, line in enumerate(lines):
    if line.startswith('## Overview'):   
        lines[i] = lines[i]+data
   
f.truncate()
f.seek(0)                                          
for line in lines:
    f.write(line)
    
