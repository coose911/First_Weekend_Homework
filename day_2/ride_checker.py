height = 180
age = 8
mood = 'happy'
is_old_enough = age > 9
is_tall_enough = height > 100

if (is_tall_enough and is_old_enough) or mood == 'happy':
    print('you may enter the ride!')
else:
    print('NO ENTRY')
    