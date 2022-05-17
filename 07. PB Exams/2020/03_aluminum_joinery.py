joinery_num = int(input())
joinery_type = input()
receiving = input()
delivery = 60
price = 0
total_price = 0

if joinery_type == "90X130":
    price = 110
    if 60 >= joinery_num > 30:
        price *= 0.95
    elif joinery_num > 60:
        price *= 0.92
elif joinery_type == "100X150":
    price = 140
    if 80 >= joinery_num > 40:
        price *= 0.94
    elif joinery_num > 80:
        price *= 0.90
elif joinery_type == "130X180":
    price = 190
    if 50 >= joinery_num > 20:
        price *= 0.93
    elif joinery_num > 50:
        price *= 0.88
elif joinery_type == "200X300":
    price = 250
    if 50 >= joinery_num > 25:
        price *= 0.91
    elif joinery_num > 50:
        price *= 0.86
cost = joinery_num * price
if receiving == "With delivery":
    total_price = cost + delivery
elif receiving == "Without delivery":
    total_price = cost
if joinery_num > 99:
    total_price *= 0.96
if joinery_num < 10:
    print("Invalid order")
else:
    print(f'{total_price:.2f} BGN')
