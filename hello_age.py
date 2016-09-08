print('What is your name?')
myName =  raw_input()

print('Welcome, ' +myName+ ', what is your age?')
while True:
    try:
        myAge = raw_input()
        val = int(myAge)
        break
    except ValueError:
        print('Please enter an integer value')
    

while True:
    print('Please enter your birth month\n')
    print(' 1 - Jan\n 2 - Feb\n 3 - Mar\n 4 - Apr\n 5 - May\n 6 - Jun\n 7 - Jul\n 8 - Aug\n 9 - Sep\n 10 - Oct\n 11 - Nov\n 12 - Dec')
    birthMonth = int(raw_input())

    if (birthMonth > 0 and birthMonth <=7):
          birthYear = 2016 - int(myAge)
          break
    elif (birthMonth >= 8 and birthMonth < 13):
          birthYear = 2016 - int(myAge) - 1
          break
    else:
          print('not a valid birth month')
      

if birthYear < 0:
    print('You were born in '+ str(birthYear) + 'B.C. , immortal')
elif myAge > 249:
    print('You were born in '+ str(birthYear)+ ', goldie oldie')
elif myAge < 250:
    print('You were born in '+ str(birthYear))
