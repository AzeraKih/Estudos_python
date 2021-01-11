##Create two variables 'x', and 'y':
##
##'x' - positive infinity
##'y' - negative infinity
##Print 'x' and 'y' in separate lines, and also print the output of the
##math.isinf function, obtained when 'x' and 'y' are passed as arguments, in
##separate lines.

import math

x = float("inf")
y = float("-inf")

print(x)
print(y)
print(math.isinf(x))
print(math.isinf(y))
