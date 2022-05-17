movie = input()
type_of_order = input()
ticket_number = int(input())

if movie == "John Wick":
    if type_of_order == "Drink":
        price = 12
    elif type_of_order == "Popcorn":
        price = 15
    elif type_of_order == "Menu":
        price = 19
elif movie == "Star Wars":
    if type_of_order == "Drink":
        price = 18
    elif type_of_order == "Popcorn":
        price = 25
    elif type_of_order == "Menu":
        price = 30
elif movie == "Jumanji":
    if type_of_order == "Drink":
        price = 9
    elif type_of_order == "Popcorn":
        price = 11
    elif type_of_order == "Menu":
        price = 14

total_price = ticket_number * price
if ticket_number >= 4 and movie == "Star Wars":
    total_price *= 0.70
elif ticket_number == 2 and movie == "Jumanji":
    total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")