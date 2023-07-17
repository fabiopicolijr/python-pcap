# read more than one line at a time means better performance, but remember that
#  reading all lines at once may crash the program if the text is too big

try:
    stream = open('animals.txt')
    # your code goes here
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

try:
    stream = open('animalsssd.txt')
    # your code goes here
    stream.close()
except Exception as e:
    print('An error occurred: ', e)


try:
    stream = open('animals.txt')
    print(stream.read())
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

print('AQUI')
try:
    stream = open('animals.txt')
    print(stream.read(1))
    print(stream.read(2))
    stream.close()
except Exception as e:
    print('An error occurred: ', e)


try:
    stream = open('animals.txt')
    print(stream.read(10000))
    print(stream.read(1))
    stream.close()
except Exception as e:
    print('An error occurred: ', e)


try:
    stream = open('animals.txt')
    character = stream.read(1)
    while character != '':
        print(character, end='-')
        character = stream.read(1)
    stream.close()
except Exception as e:
    print('An error occurred: ', e)


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


try:
    stream = open('animals.txt')
    counter = 0
    line = stream.readline()
    while line != '':
        counter += 1
        print(line, end='-')
        line = stream.readline()
    stream.close()
    print('\nNumber of lines:', counter)
except Exception as e:
    print('An error occurred: ', e)


try:
    stream = open('animals.txt')
    lines = stream.readlines()
    print('Content of the lines var:', lines)
    print('Number of lines in the file:', len(lines))
    for line in lines:
        print(line, end='')
    stream.close()
except Exception as e:
    print('An error occurred: ', e)


try:
    stream = open('animals.txt')
    lines = stream.readlines(2)
    while len(lines) != 0:
        for line in lines:
            print(line, sep='')
        lines = stream.readlines(2)
    stream.close()
except Exception as e:
    print('An error occurred: ', e)


try:
    stream = open('animals.txt')
    for line in stream:
        print(line, end='')
except Exception as e:
    print('An error occurred: ', e)

