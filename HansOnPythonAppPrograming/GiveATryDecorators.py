##def outer(func):
##    def inner():
##        print("Accessing :", 
##                  func.__name__)
##        return func()
##    
##    return inner
##
##@outer
##def greet():
##    return 'Hello!'
##print(greet())
##
##
##
##def greet(msg):
##    return ("Accessed the function -'greet' with arguments ('" + msg + "',) {}")
##
##print(greet("Hello world"))


##def log(func):
##    def inner(*args, **kwdargs):
##        str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__,
##                                                                                args,
##                                                                            kwdargs)
##        return str_template + "\n" + str(func(*args, **kwdargs))
##    return inner
##
##@log
##def average(n1,n2,n3):
##    return (n1+n2+n3)/3


##def bold_tag(func):    
##    def inner(*args, **kwdargs):
##        return '<b>'+func(*args, **kwdargs)+'</b>'        
##    return inner
##
##def italic_tag(func):
##    def inner(*args, **kwdargs):
##        return '<i>'+func(*args, **kwdargs)+'</i>'        
##    return inner
##
##def say(msg):
##    return msg
##say = italic_tag(say)


##@italic_tag
##@bold_tag
##def greet():
##    return input()


##def star(func):
##    def inner(args, **kwargs):
##        print("" * 3)
##        func(args, **kwargs)
##        print("" * 3)
##    return inner
##
##def percent(func):
##    def inner(*args, **kwargs):
##        print("%" * 3)
##        func(*args, **kwargs)
##        print("%" * 3)
##    return inner
##
##@star
##@percent
##def printer(msg):
##    print(msg)
##    
##printer("Hello")


##def smart_divide(func):
##    def wrapper(*args):
##        a, b = args
##        if b == 0:
##            print('oops! cannot divide')
##            return
##        return func(*args)
##    return wrapper
##
##@smart_divide
##def divide(a, b):
##    return a / b
##
##print(divide.__name__)
##print(divide(4, 16))
##print(divide(4, 0))

