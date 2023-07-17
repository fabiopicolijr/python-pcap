# the command starts with the separator
print(' '.join(['This is', 'a spectacular', 'place to be']))

# [with argument] will create a list with the separator
print('How many\tstrings\nwill you see?'.split(' '))
# [without argument] will create a list with the all words separated and will remove scape characters
print('How many\tstrings\nwill you see?'.split())

# sorted creates a sorted copy
print('\nSORTED')
names1 = ['Adam', 'Kate', 'Barbara', 'Donna']
names_sorted = sorted(names1)  # sorted=classificado [alfabeto]
print(names_sorted)
print(names1)

# sorts the original list
print('\nSORT')
names = ['Adam', 'Kate', 'Barbara', 'Donna']
names.sort() # !IMPORTANT return None
print(names)



