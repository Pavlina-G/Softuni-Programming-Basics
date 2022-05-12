month = input()
nights = int(input())
price_studio = 0
price_apart = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apart = 65
    if 7 < nights <= 14:
        price_studio *= 0.95
    elif nights > 14:
        price_studio *= 0.70
        price_apart *= 0.90

elif month == "June" or month == "September":
    price_studio = 75.20
    price_apart = 68.70
    if nights > 14:
        price_studio *= 0.80
        price_apart *= 0.90

elif month == "July" or month == "August":
    price_studio = 76
    price_apart = 77
    if nights > 14:
        price_apart *= 0.90

cost_studio = nights * price_studio
cost_apart= nights * price_apart

print(f'Apartment: {cost_apart:.2f} lv.')
print(f'Studio: {cost_studio:.2f} lv.')







    