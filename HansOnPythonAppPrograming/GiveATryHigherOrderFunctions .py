##Define a function named detecter, with one parameter element and
##returns an inner function isIn.isIn accepts one parameter, sequence
##and returns True or False after checking the presence of element in
##sequence.Create two closure functions detect30 and detect45 using
##detecter.Pass 30 to detect30 and 45 to detect45 for implementationUse
##the 'Test against custom input' box below to output your result for
##debugging - Provide a set of integers separated by comma
##(refer test case samples below) to display the output / error


##def detecter(num):
##    def isIn(seq):
##        return (num in seq)
##    return isIn
##
##
##detect30 = detecter(30)
##detect45 = detecter(45)
##print(detect30((0, 2, 30)))


##Define a function named factory, with a variable n initialized to zero
##and two inner functions namely current and counter.current must return
##current value of n.counter must increment the value of n by one.Hint:
##check the closure functions f_current and f_counter and return the
##current and counter functions from factory accordinglyUse the
##'Test against custom input' box below to output your result for
##debugging - Provide an integer (refer test case samples below)
##to display the output / error

##def factory(nu):
##    global num
##    num = nu
##    def f_current():
##        return num
##    def f_counter():
##        global num
##        num += 1
##        return f_current()
##    return f_current, f_counter
##
##
##f_current, f_counter = factory(int(1))
##print(f_current())
##print(f_counter())
##print(f_counter())
##print(f_counter())
##print(f_current())
##print(f_counter())
##print(f_current())



##def multipliers():
##    return [lambda x : i * x for i in range(4)]
##
##print([m(2) for m in multipliers()])

##def outer(x, y):
##
##    def inner1():
##        return x+y
##
##    def inner2():
##        return x*y
##
##    return (inner1, inner2)
##
##
##(f1, f2) = outer(10, 25)
##
##print(f1())
##print(f2())
