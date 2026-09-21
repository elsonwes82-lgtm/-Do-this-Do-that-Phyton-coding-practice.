def do_this():
    print('Doing this')

def do_that():
    print('Doing that')
    
answer = input('Do this or that?')

if answer == 'this':
   do_this()
elif answer == 'that':
    do_that()
else:
    print('Invalid Input')
