print(len('hi there!'))
print(len(''))

print('hi there'[0])  # starts with 0 (position)

print('hi there'[1:])  # i there

print('hi there'[:2])  # h1

print('hi there'[3:6])  # !IMPORTANT prints 'the' [start after, length(not consider start)]

print('I\'m Adrian')  # escape character

print(ord('a'))  # prints CHR number

print(chr(97))  # prints the character

test_string = '''Line 1
Line 2'''
print(len(test_string))  # !IMPORTANT we expect 12, but python count the special break line (line feed \n) character
# (invisible)

print(2 * 'ccc')  # IMPORTANT prints 'cccccc'  cooool!

for char in 'hello from the world of python':
    print(char, end='|')

print()
print(min('hellofromtheworldofpython'))  # smallest character from a sequence  'd' in this case
print(max('hellofromtheworldofpython'))  # biggest character from a sequence  'y' in this case
