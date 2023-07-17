lambda_func = lambda i: i * 2
initial_list = [1, 2, 3, 4, 5]

map(lambda_func, initial_list)

map_result = map(lambda_func, initial_list)
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))
# print(next(map_result))

map_result = map(lambda_func, initial_list)
for element in map_result:
    print(element, end=',')

map_result = map(lambda_func, initial_list)
print(list(map_result))

lambda_func = lambda i: i * 2
initial_list = [1, 2, 3, 4, 5]
map_result = map(lambda_func, initial_list)
print(list(map_result))

print(list(map(lambda i: i * 2, [1, 2, 3, 4, 5])))

print(list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8])))

emails = [
    'frank@gmail.com',
    'i love python',
    '98237434',
    'jonsmith@yahoo.com',
    'whereareyou@mywebsite.co.uk',
    'fs3dfss'
]
print(list(filter(lambda i: '@' in i, emails)))
