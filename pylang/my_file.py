file = open("data/haha.txt","r+")
lines = file.readlines()
for line in lines:
    print(line)
if file.writable(): 
    file.write("\nappend a new line....")
else:
    print("file cannot be written")
file.close()