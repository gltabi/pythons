def collatz(number):
    if number % 2 == 0:
        print number // 2
        return number // 2

    else:
        print 3 * number + 1
        return 3 * number + 1

def execution():

    print('Please type an integer')
    intGiven = raw_input()

    try:
        intGiven = int(intGiven)

    except ValueError:
        print('Error: please enter an integer')
        execution()
        
    result = collatz(intGiven)

    while result != 1:
        result=collatz(result)

execution()


