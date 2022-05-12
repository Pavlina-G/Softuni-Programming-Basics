budget = int(input())
season = input()
numbers_of_fisherman = int(input())
price = 0

if season == "Spring":
    price = 3000
    if numbers_of_fisherman <= 6:
        price *= 0.9
    elif 7 <= numbers_of_fisherman <= 11:
        price *= 0.85
    elif numbers_of_fisherman >= 12:
        price *= 0.75
elif season == "Summer" or season == "Autumn":
    price = 4200
    if numbers_of_fisherman <= 6:
        price *= 0.9
    elif 7 <= numbers_of_fisherman <= 11:
        price *= 0.85
    elif numbers_of_fisherman >= 12:
        price *= 0.75
elif season == "Winter":
    price = 2600
    if numbers_of_fisherman <= 6:
        price *= 0.9
    elif 7 <= numbers_of_fisherman <= 11:
        price *= 0.85
    elif numbers_of_fisherman >= 12:
        price *= 0.75

if numbers_of_fisherman % 2 == 0 and season != "Autumn":
        price *= 0.95
difference = abs(price - budget)

if budget >= price:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')





