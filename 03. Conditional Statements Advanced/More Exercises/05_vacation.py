budget = float(input())
season = input()
location = ""
stay = ""
price = 0

if budget <= 1000:
    stay = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    stay = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
else:
    stay = "Hotel"
    price = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {stay} - {price:.2f}")