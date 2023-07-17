

try:
    stream = open('nonexistent.txt')
    stream.close()
except Exception as e:
    print('An error occurred: ', e)


try:
    stream = open('nonexistent.txt')
    stream.close()
except Exception as e:
    print(e.errno)


from os import strerror

try:
    stream = open('nonexistent.txt')
    stream.close()
except Exception as e:
    print(strerror(e.errno))