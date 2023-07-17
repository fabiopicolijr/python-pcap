# Exceptions: Is a event of the program
# Some errors type (exceptions): IndentationError, ValueError, ZeroDivisionError

try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1 / value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0. An division by 0 is not possible')
except:
    print('Something goes wrong')

