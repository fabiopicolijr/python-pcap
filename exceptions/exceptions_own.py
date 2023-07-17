class AnimalValueError(ValueError):
    pass


def produce_animal_sound(animal_type):
    if animal_type == 'DOG':
        print('Woof, woof!')
    elif animal_type == 'Cat':
        print('Meow!')
    else:
        raise AnimalValueError('Incorrect animal type!')

#
# produce_animal_sound('DOG')  # Woof, woof!
#
# produce_animal_sound('PIG')
# --------------------------------------------------------------------------- AnimalValueError Traceback (most recent
# call last) ~\AppData\Local\Temp/ipykernel_2456/2314978789.py in <module> ----> 1 produce_animal_sound('PIG')
# ~\AppData\Local\Temp/ipykernel_2456/2163390556.py in produce_animal_sound(animal_type) 8 print('Meow!') 9 else:
# ---> 10 raise AnimalValueError('Incorrect animal type!') AnimalValueError: Incorrect animal type!


class UserActionException(Exception):  # cool
    def __init__(self, message='', user_id=''):
        Exception.__init__(self)
        self.user_id = user_id
        self.message = message

    def __str__(self):
        return type(self).__name__ + ' occurred. Error message: ' + self.message + ', userId: ' + self.user_id


def say_hello(name, user_id):
    if name == '':
        raise UserActionException('empty name!', user_id)
    print('Hello', name)


# try:
#     say_hello('Adam', 'DT324')
#     say_hello('', 'DT324')
# except Exception as e:
#     print(e)


# Hello Adam UserActionException occurred.Error message: empty name!, userId: DT324


class EmptyNameUserActionException(UserActionException):
    def __init__(self, user_id=''):
        super().__init__('An empty name was provided', user_id)


def say_hello(name, user_id):
    if name == '':
        raise EmptyNameUserActionException(user_id)
    print('Hello', name)

try:
    say_hello('Adam', 'DT324')
    say_hello('', 'DT324')
except Exception as e:
    print(e)

# Hello Adam
# EmptyNameUserActionException occurred. Error message: An empty name was provided, userId: DT324
