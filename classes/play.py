# class A:
#     x = 'x'
#
#     def alarm(self):
#         print('a' + self.x)
#
#
# class B(A):
#     def alarm(self):
#         super().alarm()
#
#
# class C(B):
#     x = 'y'
#
#
# C().alarm()
#
#
# class A:
#     b = 1
#
#     def __init__(self):
#         self.c = 0
#
#
# print(hasattr(A, 'c'))
#
#
#
# import random
# print(dir(random))
#
# b = 3
# a = 2 ** 3
# print(a)
#
# # print('20' > '8' or '20' > 8)
#
# txt = 'aga aga aga aga'
# print(txt.find('aga'))
#
# print('TESTE')
# txt = 'aga  aga'
# print(txt.rfind('aga'))
#
# # for item in open('file.txt', 'rt'):
# #     pass
#
#
# class Car():
#     def __init__(self, initial_speed=0):
#         self.speed = initial_speed
#
#     def slow_down(self):
#         self.speed -= 5
#
# print(Car())


def float_function(n: float):
    print(n)


def int_function(n: int):
    print(n)


def str_function(n: str):
    print(n)


float_function('1,0')

# int_function('1.0')
#
# str_function(1.0)

a = float('5.0')
print(a)

print('AQUi')


def teste(x: []):
    print('x:', x)
    x += 5
    return x


print(teste([int(bytearray(10)[0])]))

print(list(map(lambda x: x + 5, [int(bytearray(10)[0])])))
