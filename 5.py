thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
  print(x)
  thisset.add("cat")

print(thisset)
thisset.remove("banana")

print(thisset)