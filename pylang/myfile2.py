import os
import sys
 
output_file  = sys.argv[1]
shortvin = sys.argv[2]
longvin = sys.argv[3]
 

template = "insert into tab1 values('%s','%s','%s')"%("aab","aaaa","cccc")
f1 = open(output_file,"w+")
f1.write(template)
f1.close()
print("done")