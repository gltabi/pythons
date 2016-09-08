toRemb = []

while True:
    print('Please enter list item ' + str(len(toRemb)+1) + ', or press Enter key to end list')
    name = raw_input()

    if name == '':
        break

    toRemb = toRemb + [name]

print('On your list:')

for name in toRemb:
    print('     ' + name)
