class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count


class Car(LandVehicle):
    pass


my_vehicle = Vehicle(50)
my_land_vehicle = LandVehicle(50, 4)
my_car = Car(60, 4)

# ISINSTANCE
print('[ISINSTANCE]')
print(isinstance(my_vehicle, Vehicle))
print(isinstance(my_land_vehicle, Vehicle))
print(isinstance(my_car, Vehicle))
print(isinstance(my_vehicle, LandVehicle))
print(isinstance(my_land_vehicle, LandVehicle))
print(isinstance(my_car, LandVehicle))
print(isinstance(my_vehicle, Car))
print(isinstance(my_land_vehicle, Car))
print(isinstance(my_car, Car))

# IS.1 : IS search differently from ==
print('\n[IS.1]')
my_vehicle = Vehicle(50)
my_new_vehicle = my_vehicle

print(my_vehicle is my_new_vehicle)  # reference, same value
print(my_vehicle.__dict__, my_new_vehicle.__dict__)
my_vehicle.speed = 30
print(my_vehicle.__dict__, my_new_vehicle.__dict__)

# IS.2
print('\n[IS.2]')
my_vehicle = Vehicle(50)
my_new_vehicle = Vehicle(50)

print(my_vehicle is my_new_vehicle)  # different object
print(my_vehicle.__dict__, my_new_vehicle.__dict__)
my_vehicle.speed = 30
print(my_vehicle.__dict__, my_new_vehicle.__dict__)

# IS.3
print('\n[IS.3]')
first_num = 5
second_num = 5
print(first_num is second_num)
first_number = 5
second_number = 2
second_number += 3
print(first_number is second_number)

# IS.4
print('\n[IS.4]')
first_str = 'hello'
second_str = 'hello'
print(first_str is second_str)
first_string = 'hello'
second_string = 'hell'
second_string += 'o' # ❗strings are immutable:  python creates a new object in the memory here.
print(first_string is second_string)  # False 😮
print(first_string == second_string)  # True
print(first_string, second_string)