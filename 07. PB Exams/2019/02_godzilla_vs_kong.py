budget = float(input())
extras = int(input())
price_clothing = float(input())
decor = budget * 0.10
total_price = extras * price_clothing
if extras > 150:
    total_price *= 0.90
total_cost = total_price + decor
difference = abs(total_cost - budget)
if budget >= total_cost:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
