# teste 1
class MyEx(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)


try:
    raise MyEx('wrong!')
except Exception as e:
    print(e)

msg = 'teste'

teste = ()
teste = (msg,)

print(teste)


# teste 2
x = 2
try:
  print(x > 3)
  print("d")
except BaseException as e:
  print("a", e)
else:
  print("b")
finally:
  print("c")


  def a():
      hey = 5

      def b():
          print(hey)

      return b


  x = a()
  print(x())

print(__name__)


class Art():
    masterpiece = 'John'

    def __init__(self):
        self.name = 'One'


print(Art().__dict__)


class A:
    x = 'x'

    def alarm(self):
        print('a' + self.x)


class B(A):
    def alarm(self):
        super().alarm()


class C(B):
    x = 'y'


C().alarm()


class Dog:
    def __init__(self, breed='none'):
        self.breed = breed

    def set(self, breed='labrador'):
        self.breed = breed
        return self.breed


puppy = Dog()
friend = puppy
friend.set()
print(puppy.breed)


class A:
    b = 1

    def __init__(self):
        self.c = 0


print(hasattr(A(), 'c'))


class X:
    Y = 1

    def __init__(self):
        self.z = 0


print(hasattr(X, 'z'))

import random
print(dir(random))

# print('20' > '8' or '20' > 8)

class A:
    b = 'b'


def __init__(self):
    self.c = 'c'
    d = self.c


a = A()
print(a.d)