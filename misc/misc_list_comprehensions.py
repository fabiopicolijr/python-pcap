numbers = []
for i in range(1, 101):
    numbers.append(i)

print('Numbers:', numbers)


# numbers = [for i in range(1, 101)]  # ERROR


numbers = [i for i in range(1, 101)]



print('Numbers:', numbers)


numbers = [i for i in range(1, 101) if i % 3 != 0]


print('Numbers:', numbers)


numbers = [0 if i % 2 == 0 else 1 for i in range(100)]


print('Numbers:', numbers)


table = [[i for i in range(1, 6)] for j in range(5)]
print(table)