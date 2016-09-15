import key_mapping
import os
import time
#import Image

#image = Image.open('arrisremote_labelled.jpg')
#image.show()

print('Input a sequence to be transmitted')
print('Please enter milliseconds between each command')
timeBetween = raw_input()
print(timeBetween + ' millisecond delay')
timeBetween = float(timeBetween)

print('Command numbers are labelled according to the image')

repeat = 'n'
while(repeat == 'n'):
    print('Please enter the command numbers separated by a space')
    command = raw_input()
    print(command + 'entered')
    command = command.split(' ')

    arraySize = len(command)

    repeat = 'y';

    while(repeat == 'y'):
        for i in range(arraySize):
            time.sleep(timeBetween)
            toEnter = ('irsend SEND_ONCE' + getRemoteName(command[i]) + keys[command[i]])   
            os.system(toEnter)

        print('repeat sequence? y/n')
        repeat = raw_input()

