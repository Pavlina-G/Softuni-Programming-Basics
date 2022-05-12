budget = float(input())
season = input()
place = ""
destination = ""
cost = 0

if season == "summer":
    place = 'Camp'
    if budget <= 100:
        destination = "Bulgaria"
        cost = 0.30 * budget
    elif 100 < budget <= 1000:
        destination = "Balkans"
        cost = 0.40 * budget

elif season == "winter":
    place = 'Hotel'
    if budget <= 100:
        destination = "Bulgaria"
        cost = 0.70 * budget
    elif 100 < budget <= 1000:
        destination = "Balkans"
        cost = 0.80 * budget

if budget > 1000:
    place = "Hotel"
    destination = "Europe"
    cost = 0.90 * budget

print(f'Somewhere in {destination}')
print(f'{place} - {cost:.2f}')