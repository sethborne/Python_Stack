def multiplicationTable(tableSize):
    for row in range(0, tableSize + 1):
        # print row
        rowString = ""
        if row == 0:
            rowItemCount = 0
            for stringItem in range(0, tableSize + 1):
                # print "first Row"
                if rowItemCount == 0:
                    rowString += "x"
                else:
                    rowString += " " + str(rowItemCount)
                rowItemCount += 1
            print rowString
        else:
            for numItem in range(0, tableSize + 1):
                length = len(rowString)
                if length == 0:
                    rowString += str(row) + " "
                else:
                    stringItem = row * numItem
                    rowString += str(stringItem) + " "
            # print row
            print rowString
multiplicationTable(12)