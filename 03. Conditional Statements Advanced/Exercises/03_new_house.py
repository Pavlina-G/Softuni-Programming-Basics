flowers = input()
number_of_flowers = int(input())
budget = int(input())
price = 0

if flowers == "Roses":
    price = 5.00
    if number_of_flowers > 80:
        price *= 0.90
elif flowers == "Dahlias":
    price = 3.80
    if number_of_flowers > 90:
        price *= 0.85
elif flowers == "Tulips":
    price = 2.80
    if number_of_flowers > 80:
        price *= 0.85
elif flowers == "Narcissus":
    price = 3.00
    if number_of_flowers < 120:
        price = price + (price * 0.15)
elif flowers == "Gladiolus":
    price = 2.50
    if number_of_flowers < 80:
        price = price + (price * 0.20)
cost = number_of_flowers * price
difference = abs(cost-budget)

if cost <= budget:
    print(f'Hey, you have a great garden with {number_of_flowers} {flowers} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')

