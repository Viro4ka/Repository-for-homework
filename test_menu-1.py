import random 
from random import randint

dishes = input("Введість страву до вечері (через кому)")
print('Ви замовили: ' + dishes)
list_of_dishes = dishes.split(", ")
print(list_of_dishes)
total_price = 0
for dish in list_of_dishes:
    price = randint(1, 100)
    total_price = total_price + price
    print(f"{dish} ....... {price} грн")
print(f"Загальна сума ....... {total_price}")