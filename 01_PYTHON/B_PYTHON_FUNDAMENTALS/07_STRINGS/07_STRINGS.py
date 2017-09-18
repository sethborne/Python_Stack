print "This is a sample string"

name = "Zen"
print "My Name is " + name

firstName = "Zenny"
lastName = "Coderbyte"
print "My Name is {} {}".format(firstName, lastName)

hw = "hello %s " % "world"
print hw

x = "Hello World Hello World"
y = "JustAlpha"
z = "123456789"
a = "abcdefghi"
b = "ABCDEFGHI"
print x.upper()
# output - hello world

print x.count("Hello")
print x.endswith("World")
print x.find("Hello")
print "--------------- IS ALPHA NUMERIC ---------------"
print "Is longer than 0 and all chars are alphanumeric = " + str(x.isalnum())
print "Is longer than 0 and all chars are alphanumeric = " + str(y.isalnum())
print "Is longer than 0 and all chars are alphanumeric = " + str(z.isalnum())
#alpha chars only
print "--------------- IS ALPHA ---------------"
print "Is longer than 0 and all chars are alpha = " + str(x.isalpha())
print "Is longer than 0 and all chars are alpha = " + str(y.isalpha())
print "Is longer than 0 and all chars are alpha = " + str(z.isalpha())
print "--------------- IS DIGIT ---------------"
print "Is longer than 0 and all chars are digit = " + str(x.isdigit())
print "Is longer than 0 and all chars are digit = " + str(y.isdigit())
print "Is longer than 0 and all chars are digit = " + str(z.isdigit())
print "--------------- IS LOWER ---------------"
print "Is longer than 0 and all chars are lower = " + str(x.islower())
print "Is longer than 0 and all chars are lower = " + str(y.islower())
print "Is longer than 0 and all chars are lower = " + str(z.islower())
print "Is longer than 0 and all chars are lower = " + str(a.islower())
print "Is longer than 0 and all chars are lower = " + str(b.islower())
print "--------------- IS UPPER ---------------"
print "Is longer than 0 and all chars are upper = " + str(x.isupper())
print "Is longer than 0 and all chars are upper = " + str(y.isupper())
print "Is longer than 0 and all chars are upper = " + str(z.isupper())
print "Is longer than 0 and all chars are upper = " + str(a.isupper())
print "Is longer than 0 and all chars are upper = " + str(b.isupper())
print "--------------- IS JOIN LIST ---------------"
print "--------------- IS SPLIT ---------------"
print a.split("e")