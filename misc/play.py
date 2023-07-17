numbers = [n for n in range(1, 101)]

numbers = [n for n in range(100) if n % 3 == 0]

print(numbers)

numbers = [0 if n % 2 == 0 else 1 for n in range(0, 101) if n % 3 == 0]

print(numbers)


table = [[i for i in range(1, 6)] for j in range(5)] # ‼‼ COOL
print(table)

table = [['*' for i in range(0, 6)] for j in range(5)] # ‼‼ COOL
print(table)

table = [['o'*i for i in range(0, 6)] for j in range(5)] # ‼‼ COOL
print(table)

table = [[f'o{i}' for i in range(0, 6)] for j in range(5)] # ‼‼ COOL
print(table)

# table = [['o'+i for i in range(0, 6)] for j in range(5)] # ‼‼ [ERROR]
# print(table)
#
#
#
# table = [[* for i in range(0, 6)] for j in range(5)] # ‼‼ [ERROR]
# print(table)


emails = [
    'frank@gmail.com',
    'i love python',
    '98237434',
    'jonsmith@yahoo.com',
    'whereareyou@mywebsite.co.uk',
    'fs3dfss'
]

print(list(filter(lambda i: '@' in i, emails)))

try:
    stream = open('animals.txt')
    counter = 0
    character = stream.read(1)
    while character != '':
        counter += 1
        print(character, end='-')
        character = stream.read(1)
    stream.close()
    print('\nNumber of characters:', counter)
except Exception as e:
    print('An error occurred: ', e)

my_list = [1,2,3,4,5,6]

for i in my_list:
    print(i, end='\t')

print('TESTE')
for i in range(3):
    print(i)

print('TESTE2')
print(2 ** 2)