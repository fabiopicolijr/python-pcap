# the diamond problem is solved by MRO in Python.

# ‼MRO, method resolution order
# 1. Look inside the object itself
# 2. If not found, look in the superclasses from left to right
# 3. If not found, show an error

class Vehicle:
    def show_power_type(self):
        print('I can use power from various sources')


class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print('I can use power from electricity')


class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print('I can use power from petrol')


class HybridCar(ElectricVehicle, PetrolVehicle):
    pass


my_toyota_yaris = HybridCar()
my_toyota_yaris.show_power_type()
