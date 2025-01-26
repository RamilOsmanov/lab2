car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"color": "black"
}

x = car.items()

print(x) 

car["year"] = 2020

print(x) 
car.update({"color": "red"})
print(x)
car.pop("model")
print(car)
for i in car:
  print(i)
  car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = car.copy()
print(mydict)
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])