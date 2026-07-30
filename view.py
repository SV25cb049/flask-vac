import json
with open ('students.json','r') as file:
    data= json.load(file)

for i in data:
    print(i)