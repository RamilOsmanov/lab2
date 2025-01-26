tl = ["apple", "cat", "20", "+ 30", 50]
print(tl)
print(tl[0])
print(tl[2:5])
tl[1]= "dog"
print(tl)
thistuple = ("kiwi", "orange")
tl.extend(thistuple)
print(tl)
tl.remove("kiwi")
print(tl)
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
thislist.sort()
print(thislist)
mylist = thislist.copy()
print(mylist)
listlet = ["a", "b", "c"]
listdig = [1, 2, 3]

list3 = listdig + listlet
print(list3)