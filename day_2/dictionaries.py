my_first_empty_dictionary = {}
# my_second_empty_dictioinary = dict{}


meals = {'breakfast' : 'pancakes', 'lunch' : 'jam roll', 'dinner' : 'salad'}

weird_dict = { 1 : '1', 2 : 2, 3 : False}
# print(weird_dict)

# print(meals['breakfast'])

# print('breakfast' in meals)

meals['dinner'] = 'soup'
# print(meals)

meals['supper'] = 'pancakes'
# print(meals)

# del(meals['breakfast'])
# print(meals.keys())

countries = {
    'uk': {
        'capital' : 'london',
        'population' : 1000 
    },
    'germany': {
        'capital' :'berlin',
        'population' : 100
    }
}

germany_population = countries['germany']['population']
print(germany_population)