i = 5

while i > 0:
    i = i // 2

    if i % 2 == 0:
        break
else:
    print('aqui no else')
    i+=1

print(i)

for n in range(3):
    break
else:
    n = 4

print(n)
