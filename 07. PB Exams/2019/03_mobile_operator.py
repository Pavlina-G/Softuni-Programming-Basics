term = input()
contract_type = input()
internet = input()
months = int(input())
total_price = 0

if term == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    elif contract_type == "ExtraLarge":
        price = 35.99

elif term == "two":
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79

if internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85


total_price = months * price

if term == "two":
    total_price = total_price - (3.75 / 100 * total_price)

print(f"{total_price:.2f} lv.")