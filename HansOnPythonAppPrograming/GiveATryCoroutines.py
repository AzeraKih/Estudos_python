##def nameFeeder():
##    while True:
##        fname = yield
##        print('First Name:', fname)
##        lname = yield
##        print('Last Name:', lname)
##
##n = nameFeeder()
##next(n)
##n.send('George')
##n.send('Williams')
##n.send('John')


##def stringDisplay():
##    while True:
##        s = yield
##        print(s*3)
##
##
##c = stringDisplay()
##c.send('Hi!!')


##def stringParser():
##    while True:
##        name = yield
##        (fname, lname) = name.split()
##        f.send(fname)
##        f.send(lname)
##
##def stringLength():
##    while True:
##        string = yield
##        print("Length of '{}' : {}".format(string, len(string)))
##
##
##f = stringLength(); next(f)
##
##s = stringParser()
##next(s)
##s.send('Jack Black')



##Define a coroutine function 'linear_equation', which takes two arguments 'a'
##and 'b'.Any coroutine derived from 'linear_equation', should be capable of
##taking a number as input,
##evaluate the expression 'a*(x**2) + b'
##The couroutine after evaluating the expression should
##print message like 'Expression, 3*x^2 + 4, with x being 6 equals 112'
##to user.
##Use print() instead of return for printing the output.

##def linear_equation(a, b):
##    while True:
##        #a*(x**2) + b
##        x = yield
##        print('Expression, ' + str(a) + '*x^2 + ' + str(b) +
##              ', with x being ' + str(x) + ' equals ' + str(a*(x**2) + b))
##
##l = linear_equation(1, 2)
##next(l)
##l.send(3)

##Define a Decorator 'coroutine_decorator', which can decorate any
##coroutine function.The decorator must create the coroutine, call
##'next' on it and return the coroutine that is ready for accepting
##any input.For e.g@coroutine_decoratordef linear_equation(a,b) :

##def coroutine_decorator(func):
##    def wrap(*args, **kwargs):
##        cr = func(*args, **kwargs)
##        cr.send(None)
##        return cr
##    return wrap
##
##@coroutine_decorator
##def linear_equation(a, b):
##    while True:
##        #a*(x**2) + b
##        x = yield
##        print('Expression, ' + str(a) + '*x^2 + ' + str(b) +
##              ', with x being ' + str(x) + ' equals ' + str(a*(x**2) + b))
##
##
##l = linear_equation(1, 2)
##l.send(3)


##Define 'linear_equation' and 'coroutine_decorator' functions as
##requested in previous test case.Define a coroutine function 'numberParser',
##which is capable of converting the passed input into an integer and also
##sends the integers to two linear equation coroutines - `equation1` and
##`equation2`. 'equation1' represents linear equation coroutine with a = 3
##and b = 4'equation2' represents linear equation coroutine with a = 2 and
##b = -1

def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.send(None)
        return cr
    return wrap

@coroutine_decorator
def linear_equation(a, b):
    while True:
        #a*(x**2) + b
        x = yield
        print('Expression, ' + str(a) + '*x^2 + ' + str(b) +
              ', with x being ' + str(x) + ' equals ' + str(a*(x**2) + b))

# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    while True:
        x = yield
        equation1.send(x)
        equation2.send(x)

















