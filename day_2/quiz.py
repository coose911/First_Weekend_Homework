my_number = 5
value = int(input('what number am i thinking of ?'))

while (value != my_number):
    if (value > my_number):
        print('high number, try a lower one')
    else:
        print('too low')    
    value = int(input('you missed that one, try another!'))

print('wow, how did you know')
