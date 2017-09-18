# Multiples

# Part 1 - Write code that prints all the odd numbers from 1 to 1000.  use a for loop, no lists.

for odds in range(1, 101):
    if odds % 2 == 1:
        print odds
    else:
        pass

for multiplesOfFive in range(5, 101):
    if multiplesOfFive % 5 == 0:
        print multiplesOfFive
    else:
        pass

# Sum List

# Create a program that prints the sum of all the values on the list
sum = 0
sumList = [ 1, 2, 5, 10, 255, 3 ]
for item in sumList:
    sum += item
print sum
# Average List

sum2 = 0
averageList = [ 1, 2, 5, 10, 255, 3 ]
for item in averageList:
    sum2 += item
print sum2
listLength = len(averageList)
print listLength
average = sum2 / listLength
print average