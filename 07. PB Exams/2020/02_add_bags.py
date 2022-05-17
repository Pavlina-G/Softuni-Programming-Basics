luggage_over_20kg = float(input())
kg_of_luggage = float(input())
days_to_trip = int(input())
number_of_luggage = int(input())
price = 0

if kg_of_luggage > 20:
    price = luggage_over_20kg
    if days_to_trip > 30:
        price *= 1.10
    elif 7 <= days_to_trip <= 30:
        price *= 1.15
    else:
        price *= 1.40
elif 10 <= kg_of_luggage <= 20:
    price = 0.50 * luggage_over_20kg
    if days_to_trip > 30:
        price *= 1.10
    elif 7 <= days_to_trip <= 30:
        price *= 1.15
    else:
        price *= 1.40
else:
    price = 0.20 *luggage_over_20kg
    if days_to_trip > 30:
        price *= 1.10
    elif 7 <= days_to_trip <= 30:
        price *= 1.15
    else:
        price *= 1.40
cost = number_of_luggage * price
print(f"The total price of bags is: {cost:.2f} lv.")
