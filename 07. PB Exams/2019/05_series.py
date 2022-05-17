budget = float(input())
series_number = int(input())

for series in range(1, series_number + 1):
    name = input()
    price = float(input())
    if name == "Thrones":
        price *= 0.50
    elif name == "Lucifer":
        price *= 0.60
    elif name == "Protector":
        price *= 0.70
    elif name == "TotalDrama":
        price *= 0.80
    elif name == "Area":
        price *= 0.90

    budget -= price

if budget >= 0:
    print(f"You bought all the series and left with {abs(budget):.2f} lv.")
elif budget < 0:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
