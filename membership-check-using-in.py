# Abe Lincoln
# 20 AUG 20XX
# Checking for List Membership Using in

# Create a list with several elements in it
fruits = ['kiwi', 'mango', 'apple']

# Use if statement and in operator to see if a specific fruit is contained
# in the list
desired_fruit = 'orange'
if desired_fruit in fruits:
    print(f'Congratulations, {desired_fruit} is contained in the list of fruits!')
    print(fruits)
else:
    print('Sorry, but orange is not contained in the fruits list.')
    print('Below is your current list of fruits:')
    print(fruits)
