fuel_type = input()
fuel_amount = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
cost = 0

if club_card == 'Yes':
    if fuel_type == 'Gas':
        cost = fuel_amount * (gas_price - 0.08)
        if 20 <= fuel_amount <= 25:
            cost *= 0.92
        elif fuel_amount > 25:
            cost *= 0.90
    elif fuel_type == 'Gasoline':
        cost = fuel_amount * (gasoline_price - 0.18)
        if 20 <= fuel_amount <= 25:
            cost *= 0.92
        elif fuel_amount > 25:
            cost *= 0.90
    elif fuel_type == 'Diesel':
        cost = fuel_amount * (diesel_price - 0.12)
        if 20 <= fuel_amount <= 25:
            cost *= 0.92
        elif fuel_amount > 25:
            cost *= 0.90
else:
    if fuel_type == 'Gas':
        cost = fuel_amount * gas_price
        if 20 <= fuel_amount <= 25:
            cost *= 0.92
        elif fuel_amount > 25:
            cost *= 0.90
    elif fuel_type == 'Gasoline':
        cost = fuel_amount * gasoline_price
        if 20 <= fuel_amount <= 25:
            cost *= 0.92
        elif fuel_amount > 25:
            cost *= 0.90
    elif fuel_type == 'Diesel':
        cost = fuel_amount * diesel_price
        if 20 <= fuel_amount <= 25:
            cost *= 0.92
        elif fuel_amount > 25:
            cost *= 0.90
print(f'{cost:.2f} lv.')




