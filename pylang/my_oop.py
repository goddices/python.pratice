class Person: 
    count = 1
    def __init__(self,name,age):
        Person.count = Person.count + 1
        self.name = name
        self.age = age
    def __str__(self):
        return  "name is %s age at %d" %(self.name,self.age)
    
class MyStringArray:
    def __init__(self,text):
        self.text = text
        self.array = text.split(" ") 

    def __iter__(self):
        return iter(self.array)

    def __next__(self): 
        return self.array.next()

    def __len__(self):
        return len(self.array)

    def __getitem__(self,key):
        return self.array[key]

class HeHe:
    # __new__
    def __new__(cls,s,b):
        self = object.__new__(cls)
        self.s = s
        self.b = b 
        print("calling __new__ method s&b is",s,b)
        return self
        
    def __init__(self,s,b):
        print("calling __init__ method s&b is",s,b) 


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

p1 = Person("zhufeng",3) 
p2 = Person("mengqi",2) 
print(p2.name)
print(p1)
print("Person.Count = %d" % Person.count)
print("p1 is instance of Person : ", isinstance(p1,Person))

msa1 = MyStringArray("hello, this is my new world !")
print("msa[0] is ",msa1[1])
print(len(msa1))
for item in msa1:
    print(item)
 

sb1 = HeHe("s","b")
 