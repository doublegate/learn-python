# Challenge - branch code execution based on user input

# print('Would you like to continue? ')
# cont_check = input()

cont_check = input('Would you like to continue? ')

if cont_check == 'no' or cont_check == 'n':
    print('Exiting')
elif cont_check == 'yes' or cont_check == 'y':
    print('Continuing ...')
    print('Complete!')
else:
    print('Please try again and respond with yes or no.')