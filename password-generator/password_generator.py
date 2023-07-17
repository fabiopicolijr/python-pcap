from random import random, choice, randint

program_title = '-- Password generator --'
program_instructions = '''Choose option:\n1: generate password\n2: exit the program'''


def generate_password():
    pass

def interact_password():
    length = int(input('Provide password length: '))
    include_upper = input('Use uppercase letters? (y/n): ').lower().strip() == 'y'
    include_digits = input('Use digits? (y/n): ').lower().strip() == 'y'
    include_special = input('Use special characters? (y/n): ').lower().strip() == 'y'

    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    #            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    #            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^', '_', '|']
    # password_possibilities = letters + numbers + symbols
    #
    # password_list = [choice(letters) for _ in range(pass_length)]
    # password = ''.join(password_list)
    #
    # print(f'\n\nGenerated password: {generate_password()}')


while True:
    print(program_title)
    print(program_instructions)
    user_choice = input('Your choice: ')

    if user_choice == '1':
        interact_password()
    elif user_choice == '2':
        print('Bye!')
        break
    else:
        print('Please enter a correct value')
