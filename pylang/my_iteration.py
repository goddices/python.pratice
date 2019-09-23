def fab(max): 
   n, a, b = 0, 0, 1 
   L = [] 
   while n < max: 
       L.append(b) 
       a, b = b, a + b 
       n = n + 1 
   return L

class Fab(object): 
 
   def __init__(self, max): 
       self.max = max 
       self.n, self.a, self.b = 0, 0, 1 
 
   def __iter__(self): 
       return self 
 
   def __next__(self): 
       if self.n < self.max: 
           r = self.b 
           self.a, self.b = self.b, self.a + self.b 
           self.n = self.n + 1 
           return r 
       raise StopIteration()


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


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

print(fab(100))

for x in reverse([1,3,5,7,9]):
    print(x) 
    
for n in Fab(5):
    print(n)

for n in Fab(5):
    print(n)


msa1 = MyStringArray("hello, this is my new world !")
print("msa[0] is ",msa1[1])
print(len(msa1))
for item in msa1:
    print(item)