drink = input()
sugar = input()
drink_number = int(input())
espresso = 0
cappuccino = 0
tea = 0
total_price = 0
price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = 0.90
        total_price = price * drink_number
        total_price *= 0.65
    elif sugar == "Normal":
        price = 1.00
        total_price = price * drink_number
    elif sugar == "Extra":
        price = 1.20
        total_price = price * drink_number
    if drink_number >= 5:
        total_price *= 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1.00
        total_price = price * drink_number
        total_price *= 0.65
    elif sugar == "Normal":
        price = 1.20
        total_price = price * drink_number
    elif sugar == "Extra":
        price = 1.60
        total_price = price * drink_number
elif drink == "Tea":
    if sugar == "Without":
        price = 0.50
        total_price = price * drink_number
        total_price *= 0.65
    elif sugar == "Normal":
        price = 0.60
        total_price = price * drink_number
    elif sugar == "Extra":
        price = 0.70
        total_price = price * drink_number
if total_price > 15.00:
    total_price *= 0.80
print(f"You bought {drink_number} cups of {drink} for {total_price:.2f} lv.")