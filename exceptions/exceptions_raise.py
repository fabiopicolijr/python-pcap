# raise is used in 2 situations:
#   1. when you are writing your tests
#   2. When you handle your errors [good for large apps]

def return_bigger(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError
    if b > a:
        return b
    else:
        return a


print(return_bigger(5, 3))  # 5

# print(return_bigger(5, 'b'))  # ValueError


def return_reverse(x):
    try:
        return 1 / x
    except:
        print('Something went wrong')
        raise  # ‼ message and exception


return_reverse(0)  # Something went wrong [ZeroDivisionError ]
