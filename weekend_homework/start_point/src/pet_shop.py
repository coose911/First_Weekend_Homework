# WRITE YOUR FUNCTIONS HERE

# 1
def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

# 2
def get_total_cash(total_money):
    return total_money["admin"]["total_cash"]

# 3
def add_or_remove_cash(amounts, amount):
    new_total = amounts["admin"]["total_cash"] + amount 
    amounts["admin"]["total_cash"] = new_total
    return new_total
    
# 4
def get_pets_sold(sold_pets):
    return sold_pets["admin"]["pets_sold"]

# 5
def increase_pets_sold(sold_pets, amount_sold):
    pets_sold = sold_pets["admin"]["pets_sold"] + amount_sold
    sold_pets["admin"]["pets_sold"] = pets_sold
    return pets_sold

# 6
def get_stock_count(stock_count):
    return len(stock_count["pets"])

# 7
def get_pets_by_breed(pet_shop, breed):
    pets = []
    list_pets = pet_shop["pets"]
    for pet in list_pets:
        if pet["breed"] == breed:
            pets.append(pet["breed"])
    return pets

# 8
def find_pet_by_name(pet_shop, name):
    pet_info = pet_shop["pets"]
    for pet in pet_info:
        if pet["name"] == name:
            return pet
        else:
            None

# 9
def remove_pet_by_name(pet_shop, name):
    pet_info = pet_shop["pets"]
    for pet in pet_info:
        if pet["name"] == name:
            pet_info.remove(pet)
            return

# 10
def add_pet_to_stock(pet_shop, new_pet):
    pets = pet_shop["pets"]
    pets.append(new_pet)
    return 

# 11
def get_customer_cash(customer):
    return customer["cash"]

# 12
def remove_customer_cash(customer_total, cash):
    customer_total["cash"] -= cash
    return customer_total

# 13
def get_customer_pet_count(customer):
    pet_count = customer["pets"]
    return len(pet_count)

# 14
def add_pet_to_customer(customer, new_pet):
    new_pet_added = customer["pets"]
    new_pet_added.append(new_pet)
    return len(customer["pets"])

# 15 Optional
def customer_can_afford_pet(customer, pet):
    customer_cash = customer["cash"]
    pet_price = pet["price"]
    if customer_cash >= pet_price:
        return True
    else:
        return False    

