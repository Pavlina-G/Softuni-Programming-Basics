budget = float(input())
number_statists = int(input())
clothing_price = float(input())
decor = budget * 0.1

clothing_price = number_statists * clothing_price
if number_statists > 150:
    clothing_price *= 0.9

needed_money = decor + clothing_price
difference = abs(needed_money - budget)
if needed_money > budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
