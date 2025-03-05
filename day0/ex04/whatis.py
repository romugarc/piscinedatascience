import sys

arg = len(sys.argv)
if arg < 2:
    exit(0)

arg = sys.argv[1]
try:
    arg = int(arg)
    rval = True
except ValueError:
    rval = False

assert rval == True, "argument is not an integer"

len = len(sys.argv)
assert len <= 2, "more than one argument is provided"

if arg % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd")