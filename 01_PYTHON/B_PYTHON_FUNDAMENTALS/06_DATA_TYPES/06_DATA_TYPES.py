# define a function that says hello to the name provided
# this starts a new block

def sayHello(name):
    # these lines are indented therefore part of the function
    if name:
        print 'Hello, ' + name + ' from inside the function'
    else:
        print 'No Name'
# now we're unidentified and have ended the previous block
print 'Outside of the function'

sayHello("Seth")