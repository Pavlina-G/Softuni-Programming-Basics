fuel_type = input()
fuel_tank_l = float(input())

if fuel_tank_l >= 25:
    if fuel_type == 'Diesel':
        print(f"You have enough {(fuel_type.lower())}.")
    elif fuel_type == 'Gasoline':
        print(f"You have enough {(fuel_type.lower())}.")
    elif fuel_type == 'Gas':
        print(f"You have enough {(fuel_type.lower())}.")
    else:
        print(f"Invalid fuel!")
else:
    if fuel_type == 'Diesel':
        print(f"Fill your tank with {(fuel_type.lower())}!")
    elif fuel_type == 'Gasoline':
        print(f"Fill your tank with {(fuel_type.lower())}!")
    elif fuel_type == 'Gas':
        print(f"Fill your tank with {(fuel_type.lower())}!")
    else:
        print(f"Invalid fuel!")


