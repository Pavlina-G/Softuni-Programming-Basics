days_of_stay = int(input())
type_of_room = input()
rating = input()
price = 0

if type_of_room == "room for one person":
    price = 18
elif type_of_room == "apartment":
    price = 25
    if days_of_stay < 10:
        price *= 0.70
    elif 10 <= days_of_stay <= 15:
        price *= 0.65
    elif days_of_stay > 15:
        price *= 0.50
elif type_of_room == "president apartment":
    price = 35
    if days_of_stay < 10:
        price *= 0.90
    elif 10 <= days_of_stay <= 15:
        price *= 0.85
    elif days_of_stay > 15:
        price *= 0.80

if rating == "positive":
    price *= 1.25
elif rating == "negative":
    price *= 0.90

cost = price * (days_of_stay - 1)
print(f'{cost:.2f}')
