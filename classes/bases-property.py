class Vehicle:
    pass


class Rideable:
    pass


class PetrolVehicle(Vehicle):
    pass


class Car(PetrolVehicle, Rideable):
    pass


print(Vehicle.__bases__)
print(Rideable.__bases__)
print(PetrolVehicle.__bases__)
print(Car.__bases__)
# This will return (<class '__main__.PetrolVehicle'>, <class '__main__.Rideable'>),
# as Car has two direct parent classes: PetrolVehicle and Rideable.
# ‼We cannot see Vehicle here because Car inherits from it indirectly through PetrolVehicle.
