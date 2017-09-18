# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

# Integer

# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

# String

# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

# List

# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

def testType(input):
    # print type(input)
    if type(input) is int:
        print input
        if input >= 100:
            print "That's a Big Number!"
        else:
            print "That's a Small Number!"
    elif type(input) is str:
        stringLength = len(input)
        print stringLength
        if stringLength >= 50:
            print "Long Sentence"
        else:
            print "Short Sentence"
    elif type(input) is list:
        print input
        listLength = len(input)
        if listLength >= 10:
            print "Big List!"
        else:
            print "Short List!"
        
        
# testType(100)
# testType(50)
# testType(1000)
# testType("Hey this is a String")
# testType("asdlfjjjjjjjjjjjjjjjjjjjjjjjjjjasdfjjjjjjjjjjjjjk;")
# testType([ 1, 2, 3, 4, 5 ])
# testType([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ])

testType(45)
testType(100)
testType(455)
testType(0)
testType(-23)
testType("Rubber baby buggy bumpers")
testType("Experience is simply the name we give out mistakes")
testType("Tell me and I forget. Teach me and I will remember. Involve me and I learn")
testType("")
testType([ 1, 7, 4, 21 ])
testType([ 3, 5, 7, 34, 3, 2, 113, 65, 8, 89])
testType([ 4, 34, 22, 68, 9, 13, 3, 5, 7, 9, 2, 12, 45, 923 ])
testType([])
testType(["name", "address", "phone number", "social security number"])