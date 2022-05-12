budget = float(input())
season = input()
type = ""
model = ""

if budget <= 100:
    type = "Economy class"
    if season == "Summer":
        model = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        model = "Jeep"
        price = budget * 0.65

elif 100 < budget <= 500:
    type = "Compact class"
    if season == "Summer":
        model = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        model = "Jeep"
        price = budget * 0.80

elif budget > 500:
    type = "Luxury class"
    model = "Jeep"
    price = budget * 0.90

print(type)
print(f"{model} - {price:.2f}")