# more descriptive variable names
# more descriptive prompt statements
# input validation
x = int(raw_input("prompt"))
if x == int or float:
    print x
else:
    print "that is not a number"

z = int(raw_input("prompt"))
if z == int or float :
    print z
else:
    print "lol you need a number stupid"



y = str(raw_input("prompt"))
if y == "+" :
    inputSum = x + z
    print ("%r + %r = %r") % (x, z, inputSum)
elif y == "-" :
    print min (x - z)
else:
    print "lol you need to put in an operation stupid"
