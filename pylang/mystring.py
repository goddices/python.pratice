import string
str1 = "哈哈"
print(str1.encode("utf8")) 
print(str1.encode("gb2312"))
str2 = "AaBbCc" 
print(str1.encode("utf8")) 
print(str1.encode("gb2312"))

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)