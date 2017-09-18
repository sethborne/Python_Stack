wordList = [ "hello", "world", "my", "name", "is", "Anna" ]
char = "o"
containsChar = False
newList = []

for word in wordList:
    if type(word) is str:
        containsChar = word.find(char)
        if containsChar > -1:
            newList.append(word)
            print word
            print newList
        else:
            print word + " Does not Contain Character: " + char
        # if word.count(char):
        #     print word
        # else:
        #     print "not Char"
            