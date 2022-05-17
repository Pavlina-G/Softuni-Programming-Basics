target_income = float(input())
cocktail = input()
target_acquired = False
current_income = 0

while cocktail != "Party!":
    cocktail_number = int(input())
    price = len(cocktail)
    price_order = cocktail_number * price
    if price_order % 2 != 0:
        price_order *= 0.75
    current_income += price_order
    if target_income <= current_income:
        target_acquired = True
        break
    cocktail = input()
difference = abs(current_income - target_income)
if cocktail == "Party!":
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {current_income:.2f} leva.")
if target_acquired:
    print(f"Target acquired.")
    print(f"Club income - {current_income:.2f} leva.")

