def typeList(inputList):
    newString = ""
    newSum = 0
    countIntInList = 0
    countStrInList = 0
    
    for item in inputList:
        if type(item) is int or type(item) is float:
            newSum += item
            countIntInList += 1
            print countIntInList
        elif type(item) is str:
            newString += " " + item
            countStrInList += 1
            
    listLength = len(inputList)
    print listLength
    if countIntInList == listLength:
        # print "hey"
        print "The List You Entered is of Integer Type"
    if countStrInList == listLength:
        print "The List you Entered is of String Type"
    
    strlength = len(newString)
    
    if strlength > 0:
        print "String:" + newString
    if newSum > 0:
        print "Sum: " + str(newSum)
    
typeList(["magical unicorns", 19, "hello", 98.98, "world"])

typeList([ 2, 3, 1, 7, 4, 12 ])

typeList([ "magical", "unicorns" ])