# When you pass the 'W' parameter, python will either create the file (if doesn't exists)
#  or will erase all content inside
try:
    stream = open('newfile.txt', 'w')
    stream.write('This is the first message!\n')
    stream.write('This is the second message!')
    stream.close()
except Exception as e:
    print('An error occurred:', e)


try:
    stream = open('newfile.txt', 'w')
    stream.write('This is a brand-new message!')
    stream.close()
except Exception as e:
    print('An error occurred:', e)