file = open(r"C:\Users\qxu8502\workspace\myspace\python\python-xuexi\pylang\data\haha.txt","r+",encoding='gbk')
lines = file.readlines()
for line in lines:
    print(line)
if file.writable(): 
    file.write("\nappend a new line....")
else:
    print("file cannot be written")
file.close()