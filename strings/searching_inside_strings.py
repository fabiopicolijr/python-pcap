print('ilovetravellingaroundtheworld'.index('a'))  # returns only the first index of a, first occurence

my_test = 'this is my sample string'

print(my_test.index('is'))  # !IMPORTANT if you search something that doesnt exists, return=ERROR occur
print(my_test.find('is'))   # !IMPORTANT if you search something that doesnt exists, return=-1

print('FIND')
print(my_test.find('g'))  # starts at 0
print(my_test.find('t', 0))  # starts at 0
print(my_test.find('t', 1))  # starts at 1
print(my_test.find('is', 5, 8))  # starts at 10, ends at 15

print('RFIND')  # REVERSE FIND, coool
print(my_test.rfind('t'))  # starts at 0
print(my_test.rfind('t', 0))  # starts at 0
print(my_test.rfind('t', 1))  # starts at 1
print(my_test.rfind('t', 0, 19))  # starts at 0
print(my_test.rfind('is', 5, 8))  # starts at 10, ends at 15

print('OTHERS 1')
print('Adrian'.isalnum())  # !IMPORTANT check if all is alpha-numeric
print('Adrian30'.isalnum())
print('Adrian_30'.isalnum())
print('Adrian 30'.isalnum())
print('Fabio'.isalpha())  # check if all is alphabetic
print('Pedro'.isdigit())  # check if all is digit

print('OTHERS 2')
print('Pedro'.islower())  # all lower
print('Pedro'.isupper())  # all upper
print('Pedro'.isspace())  # all space

