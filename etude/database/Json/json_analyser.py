import json

file = open("dep.json", "r")
data = json.load(file)

print(data[1])