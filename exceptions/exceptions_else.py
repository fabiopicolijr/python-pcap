try:
    value = int(input('Enter an int: '))
    print(1/value)
except:
    print('Something went wrong')
else:
    print('Everything is perfect')  # always executed when doesn't occur exceptions, shit functionality, not often used

