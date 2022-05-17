budget = float(input())
litre_oil = float(input())
day = input()
guide_price = 100

total_amount = litre_oil * 2.10
total_amount += guide_price

if day == "Saturday":
    total_amount *= 0.90
elif day == "Sunday":
    total_amount *= 0.80

diff = abs(total_amount - budget)

if total_amount <= budget:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")