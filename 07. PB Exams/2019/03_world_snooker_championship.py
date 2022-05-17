round_of_championship = input()
ticket_type = input()
ticket_number = int(input())
photo = input()
price = 0

if round_of_championship == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
elif round_of_championship == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
elif round_of_championship == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400.00

current_price = ticket_number * price

if current_price > 4000:
    current_price *= 0.75
elif 4000 >= current_price > 2500:
    current_price *= 0.90
    if photo == "Y":
        current_price += (ticket_number * 40)
    else:
        pass
else:
    if photo == "Y":
        current_price += ticket_number * 40
    else:
        pass

print(f"{current_price:.2f}")


