class Person: 
    count = 1
    def __init__(self,name,age):
        Person.count = Person.count + 1
        self.name = name
        self.age = age
    def __str__(self):
        return  "name is %s age at %d" %(self.name,self.age)
    

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

    @classmethod
    def say(cls):
        print(cls)


p1 = Person("zhufeng",3) 
p2 = Person("mengqi",2) 
print(p2.name)
print(p1)
print("Person.Count = %d" % Person.count)
print("p1 is instance of Person : ", isinstance(p1,Person)) 

sb1 = HeHe("s","b")
HeHe.say()