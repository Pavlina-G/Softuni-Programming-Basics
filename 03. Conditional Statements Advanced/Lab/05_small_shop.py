product = input()
city = input()
number = float(input())
cost = 0

if city == 'Sofia':
    if product == 'coffee':
        cost = number * 0.50
    elif product == 'water':
        cost = number * 0.80
    elif product == 'beer':
        cost = number * 1.20
    elif product == 'sweets':
        cost = number * 1.45
    elif product == 'peanuts':
        cost = number * 1.60

elif city == 'Plovdiv':
    if product == 'coffee':
        cost = number * 0.40
    elif product == 'water':
        cost = number * 0.70
    elif product == 'beer':
        cost = number * 1.15
    elif product == 'sweets':
        cost = number * 1.30
    elif product == 'peanuts':
        cost = number * 1.50

elif city == 'Varna':
    if product == 'coffee':
        cost = number * 0.45
    elif product == 'water':
        cost = number * 0.70
    elif product == 'beer':
        cost = number * 1.10
    elif product == 'sweets':
        cost = number * 1.35
    elif product == 'peanuts':
        cost = number * 1.55
print(cost)