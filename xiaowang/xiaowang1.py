import json

a=[  ]
index = 1
for i in range(2):
    a.append({ index :i+99})

    index+=1
    a.append({ index:i+99})
    index+=1
print(json.dumps(a))