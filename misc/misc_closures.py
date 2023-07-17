# A closure is a technique for implementing lexically scoped name binding in a
#   language with first-class functions

# In other words, it's a function defined inside another functions that remembers
#   the values of the outer function [easy way]

# one use for closures: to replace a simples class that has one method

def greet(text):
    def print_greet():
        print(text)

    return print_greet


say_hello = greet('Hello')
print(say_hello())


def make_multiply_closure(x):
 def multiply(y):
  return x * y

 return multiply


multiply_5 = make_multiply_closure(5)
multiply_12 = make_multiply_closure(12)

print(multiply_5(10))
print(multiply_5(20))

print(multiply_12(10))
print(multiply_12(20))