def makeCheckerboard(numValLoop, numValLengthString, firstChar, secondChar):
    count = 0
    for line in range(0, numValLoop + 1):
        if line % 2 == 0:
            # even
            newString = ""
            for lineItem in range(0, numValLengthString):
                if lineItem % 2 == 0:
                    newString += firstChar
                else:
                    newString += secondChar
            print newString
        else:
            # odd
            # print "Odd Lines"
            newString = ""
            for lineItem in range(0, numValLengthString):
                if lineItem % 2 == 0:
                    newString += secondChar
                else:
                    newString += firstChar
            print newString
        count += 1
        # print "Count: " + str(count)
        # print 
        
makeCheckerboard(10, 5, "*", " ")
print "                                                      "
makeCheckerboard(50, 65, "a ", "b ")