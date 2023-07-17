# EXCEPTIONS HIERARCHY
import sys

# BaseException
#     Exception, SystemExit, KeyboardInterrupt ...
#         ArithmeticError [ZeroDivisionError ...], LookupError [IndexError, KeyError], TypeError, ValueError ...


# sys.exit()  # SystemExit

# ctrl+D    # KeyboardInterrupt


languages = ['Java', 'Python', 'C++']

print(languages[10])  # IndexError

ages = {'Jim': 30, 'Pam': 12, 'Kevin': 33}

print(ages['Michael'])  # KeyError

age = input('What is your age? ')
print('In 10 years, you will be', age + 10)  # TypeError

age = int(input('What is your age? '))  # user inputs 'A' =  # ValueError
