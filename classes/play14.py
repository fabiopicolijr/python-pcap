def teste_function(a, b):
    return a * b


print(teste_function(1, 2))

print(teste_function(5, [1]))

print(bytearray(10000))
print(bytearray(10000)[0])
print(bytearray(10000)[1])
print(bytearray(10000)[2])
print(bytearray(10000)[3])
print(bytearray(10000)[4])

print(list(map(lambda x: x + 5, [int(bytearray(10000)[0])])))

a = lambda x: x + 5
lst = [1,2]

print(list(map(a, lst)))




print(chr(ord('a') + 2))
print(ord(chr(67)))