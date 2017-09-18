def compareLists(listOne, listTwo):
    shouldCheck = False
    iterCount = 0
    loopCount = 0
    if len(listOne) != len(listTwo):
        print "The Lists Are not the Same"
    elif len(listOne) == len(listTwo):
        shouldCheck = True
        print "The Lists Are the Same Length"
    if shouldCheck == True:
        lengthLists = len(listOne)
        for itemA in listOne:
            # print itemA
                if itemA == listTwo[loopCount]:
                    iterCount += 1
                    # print "Count: " + str(iterCount)
                # print "ItemA: " + str(itemA)
                # print "ItemB: " + str(listTwo[loopCount])
                loopCount += 1
        # print "List Length: " + str(lengthLists)
        # print "IterCount: " + str(iterCount)
        if lengthLists == iterCount:
            print "The Lists Have the Same Content"
        else:
            print "The Lists are the Same Length, but have Different Content"
                
            
        
listOneA = [ 1, 2, 5, 6, 2 ]
listTwoA = [ 1, 2, 5, 6, 2 ]
compareLists(listOneA, listTwoA)

listOneB = [ 1, 2, 5, 6, 5 ]
listTwoB = [ 1, 2, 5, 6, 5, 3 ]
compareLists(listOneB, listTwoB)

listOneC = [ 1, 2, 5, 6, 5, 16 ]
listTwoC = [ 1, 2, 5, 6, 5 ]
compareLists(listOneC, listTwoC)

listOneD = [ "celery", "carrots", "bread", "milk" ]
listTwoD = [ "celery", "carrots", "bread", "cream" ]
compareLists(listOneD, listTwoD)