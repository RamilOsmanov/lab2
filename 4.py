tp =(1,2,3)
print(tp)
print(tp[2])
print(tp[1:2])
y = list(tp)
y.append("orange")
print(y)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
thistuple = ("apple", "banana", "cherry")

(green, yellow, red) = thistuple

print(green)
print(yellow)
print(red)
for x in thistuple:
  print(x)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)