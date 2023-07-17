# MULTIPLE INHERITANCE: try to avoid, only in last result

# ‼MRO, method resolution order
# 1. Look inside the object itself
# 2. If not found, look in the superclasses from left to right
# 3. If not found, show an error

class Vehicle:
    def go(self):
        print('Going!')

    def introduce(self):
        print('I am a Vehicle')


class Flyable:
    def fly(self):
        print('Flying!')

    def introduce(self):
        print('I am a Flyable')


class Airplane(Vehicle, Flyable):
    pass


my_plane = Airplane()
my_plane.go()
my_plane.fly()
my_plane.introduce()  # MRO
