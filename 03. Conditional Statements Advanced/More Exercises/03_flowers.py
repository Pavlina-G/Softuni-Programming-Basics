chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price_chr = 0
price_rose = 0
price_tulip = 0
arranging = 2.00
total_price = 0

if season == "Spring" or season == "Summer":
    price_chr = 2
    price_rose = 4.1
    price_tulip = 2.50
    if holiday == "Y":
        price_chr *= 1.15
        price_rose *= 1.15
        price_tulip *= 1.15
    else:
        pass

elif season == "Autumn" or season == "Winter":
    price_chr = 3.75
    price_rose = 4.50
    price_tulip = 4.15
    if holiday == "Y":
        price_chr *= 1.15
        price_rose *= 1.15
        price_tulip *= 1.15
    else:
        pass

total_price = round((chrysanthemums * price_chr) + (tulips * price_tulip) + (roses * price_rose),2)
if (chrysanthemums + roses + tulips) > 20:
    total_price *= 0.80
if tulips > 7 and season == "Spring":
    total_price *= 0.95
elif roses >= 10 and season == "Winter":
    total_price *= 0.90

total_price = total_price + arranging

print(f'{total_price:.2f}')