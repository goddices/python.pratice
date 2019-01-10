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

print(fab(100))

for x in reverse([1,3,5,7,9]):
    print(x) 
    
for n in Fab(5):
    print(n)

for n in Fab(5):
    print(n)