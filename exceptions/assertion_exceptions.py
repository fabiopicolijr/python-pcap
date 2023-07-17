# Assertions are assumptions in your program that should always be true.

# USE of assertions:
#     1. For debugging / testing your code
#     2. For documenting your code
#
# DO NOT: because it's possible turning off assertions when you publish your project
#     1. Validate user input with assertions
#     2. Handle AssertionsErrors in try...except

def calculate_inverse(number):
    assert (number != 0), 'Got 0 as number'
    return 1 / number


print(calculate_inverse(0))  # AssertionsErrors
