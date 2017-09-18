# Lists
ninjas = ["Rozen", "KB", "Oliver"]
myList = ["4", ["List", "in", "a", "list"], "987"]
emptyList = []

fruits = ["apple", "banana", "orange", "strawberry"]
vegetables = ["lettuce", "cucumber", "carrots"]

fruitsAndVegetables = fruits + vegetables
print fruitsAndVegetables
salad = 3 * vegetables
print salad

drawer = ["documents", "envelopes", "pens"]
print drawer[0]
print drawer[1]
print drawer[2]

x = [ 1, 2, 3, 4, 5 ]
x.append(99)
print x

x = [ 99, 4, 2, 5, -3 ]
print x[:]
print x[1:]
print x[:4]
print x[2:4]

myList = [ 1, "Zen", "Hi" ]
print len(myList)

myList2 = [ 1, 5, 2, 8, 4 ]
myList2.append(7)
print myList2

print enumerate(myList2)
print min(myList2)
print sorted(myList2)

print myList2.extend(myList)
print myList.pop(0)
print myList2.index(1)

