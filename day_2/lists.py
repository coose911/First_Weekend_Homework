# fruits = ['apple', 'banana', 'grape', 'orange']

# print(fruits[0])
# print(fruits[-1])

# fruits[2]='mango'
# print(fruits)

# number_of_items = len(fruits)
# print(number_of_items)

# my_list = ['apple', 2, 'peanut butter', fruits]
# print(my_list)

# fruits.append('pear')
# print(fruits)
# fruits.pop()
# print(fruits)

# 1. Create an empty list called `task_list`

# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner'

# 3. Print out `task_list`

# 4. Remove the last task

# 5. Print out `task_list`

# 6. Print out the number of elements in `task_list`

task_list = []
task_list.append('make dinner')
task_list.append('go to gym')
task_list.append('brush teeth')
task_list.extend(['walk dog', 'make sandwiches'])
print(task_list)
task_list.pop()
print(task_list)
# length_of_list = len(task_list)
# print(length_of_list)
print(len(task_list))