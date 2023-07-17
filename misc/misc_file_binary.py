data = bytearray(100)
data[0] = 100

# data = bytearray(100)
# data[0] = 270 # Error because the maximum is 256


data = bytearray(10)
data[0] = 100
data[1] = 120

print('oi')
print(data[0])

try:
    stream = open('file.bin', 'wb')
    stream.write(data)
    stream.close()
except Exception as e:
    print('An error eccurred:', e)

try:
 bf = open('file.bin', 'rb')
 byte_array = bf.read()
 bf.close()
except Exception as e:
 print('An error eccurred:', e)

print(byte_array)


for byte in byte_array:
    print(hex(byte), end='')

for byte in byte_array:
    print(int(byte), end=' ')

try:
 bf = open('file.bin', 'rb')
 byte_array = bf.read(10)
 bf.close()
except Exception as e:
 print('An error eccurred:', e)

for byte in byte_array:
 print(int(byte), end=' ')