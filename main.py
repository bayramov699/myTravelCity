""" I WISH TO GO TO THIS CITIES """


MyTravelList = [
    'wisconsin',
    'athena',
    'san fransisco',
    'san martin',
    'london',
    'new york',
    'oslo',
    'stokholm',
    'new jersey',

]

client = input('Please, enter your name: ')

wishOfClient = input(f'Dear {client}, please type which city you want to travel: ')


if wishOfClient.lower() in MyTravelList:
    print(f'I want to travel {wishOfClient} too')
else:
    print('I will think about it in future')