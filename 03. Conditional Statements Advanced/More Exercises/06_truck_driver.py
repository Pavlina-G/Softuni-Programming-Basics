season = input()
km_month = float(input())

price_km = 0

if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.75
    elif season == "Summer":
        price_km = 0.90
    else:
        price_km = 1.05
elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.95
    elif season == "Summer":
        price_km = 1.10
    else:
        price_km = 1.25
elif 10000 < km_month <= 20000:
    price_km = 1.45

total_amount = km_month * price_km * 4
total_amount *= 0.90
# -10% taxes
print(f"{total_amount:.2f}")