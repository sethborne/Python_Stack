words = "It's Thanksgiving Day. It's my birthday, too!"

# Find and Replace

# print words.find("Day")
# print words.replace("Day", "Month")

# Min and Max

# x = [ 2, 54, -2, 7, 12, 98 ]
# print min(x)
# print max(x)

# First and Last

x = [ "hello", 2, 54, -2, 7, 12, 98, "world"]
firstIndexValue = x[0]
print firstIndexValue
endIndex = len(x) - 1 
print endIndex
endIndexValue = x[endIndex]

newList = [ firstIndexValue, endIndexValue ]
print newList

# New List

y = [ 19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6 ]
ySorted = sorted(y)
print ySorted
totalListLength = len(y)
print totalListLength
halfListLength = totalListLength / 2
print halfListLength
newfirstIndexValue = ySorted[0:4]
print newfirstIndexValue
y = ySorted[4:totalListLength]
newfirstIndexValue.append(y[0])
print newfirstIndexValue
y[0] = newfirstIndexValue
print y