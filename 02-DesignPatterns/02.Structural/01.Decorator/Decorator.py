from functools import wraps
def make_blink(function):
    @wraps(function)
    def decorator():
         ret=function()   
     
         return "<blink>"+ret+"</blink>"
    return decorator

@make_blink
def hello_decorator():
    """original decorator"""
    return 'hello, decorator'

print(hello_decorator())
# check the function name is the same as decorated
print(hello_decorator.__name__)
# check the docstring and main function are the same
print(hello_decorator.__doc__)