# Lambda: a simples way to write an function inline (anonymous functions)

def function_name(parameter1, parameter2):
  # instruction1
  # instruction2
  pass


var = lambda parameter1, parameter2: parameter1 * parameter2


def sum(a, b):
 return a + b


lambda a, b: a + b


lambda x, y: x + y


sum(5, 3)


another_sum = lambda a, b: a + b


def apply_func(elements, func):
 for element in elements:
  print(func(element))


my_func = lambda x: x * x
apply_func([1, 2, 3, 4, 5], my_func)


my_func = lambda x: 1/x
apply_func([1, 2, 3, 4, 5], my_func)


my_func = lambda x: 0
apply_func([1, 2, 3, 4, 5], my_func)


apply_func([1, 2, 3, 4, 5], lambda x: x * x)