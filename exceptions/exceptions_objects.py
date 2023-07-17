def return_bigger(a, b):
    try:
        if b > a:
            return b
        else:
            return a
    except Exception as e:
        print(e)
        return None


print(return_bigger(5, 'b'))  # '>' not supported between instances of 'str' and 'int' None


for subclass in BaseException.__subclasses__():
    print(subclass.__name__)

# Exception
# GeneratorExit
# SystemExit
# KeyboardInterrupt
# CancelledError
# DebuggerInitializationError


for subclass in Exception.__subclasses__():
    print(subclass.__name__)

try:
    raise Exception
except Exception as e:
    print(e.args)  # ()


try:
    raise Exception('i do not like it')
except Exception as e:
    print(e.args)  # ('i do not like it',)


try:
    raise Exception('i do not like it', 'in fact, i do not like it at all')
except Exception as e:
    print(e.args)  # ('i do not like it', 'in fact, i do not like it at all')


try:
    1/0
except Exception as e:
    print(e.args)  # ('division by zero',)


try:
    5 < 'a'
except Exception as e:
    print(e.args)  # ("'<' not supported between instances of 'int' and 'str'",)