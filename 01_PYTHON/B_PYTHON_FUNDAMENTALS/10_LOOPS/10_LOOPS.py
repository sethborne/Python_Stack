for count in range(0,5):
    print "Looping - ", count
    
myList = [ 4, "dog", 99, ["list", "inside", "another"], "hello world"]
for element in myList:
    print element
    
count = 0
while count < 5:
    print "While Looping - ", count
    count += 1
    
for val in "string":
    if val == "g":
        break
    print val

print "                      "

for val in "string":
    if val == "i":
        continue
    print val
    
class EmptyClass:
    pass
    
myString = "myTest"
for val in myString:
    pass

print "                      "

x = 3
y = x
while y > 0:
    print y 
    y = y - 1
    if y == 0:
        break
else:
    print "Final Else Statement"
    
