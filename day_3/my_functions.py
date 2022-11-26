# def greet(name):
#     return f"hello {name}"

# greeting = greet('marcus')
# greeting1 = greet(1)

# print(greeting)
# print(greeting1)


# def sums(a,b):
#     return f" a plus b is equal to {a + b}"

# adding_up = sums(3,9)    
# print(adding_up)

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]


total_eggs = 0

for chicken in chickens:
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0 # eggs have been collected

print(f"{total_eggs} eggs collected")

def egg_collector(list_of_chickens):
    total_eggs = 0
    for chicken in list_of_chickens:
        total_eggs = total_eggs + chicken["eggs"]
        # total_eggs += chicken["eggs"] #same as above 
        chicken["eggs"] = 0 #removing the eggs from the chicken
    return total_eggs

eggs_collected = egg_collector(chickens)
print(eggs_collected)   

