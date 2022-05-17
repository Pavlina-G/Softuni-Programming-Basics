city = input()
type_of_stay = input()
vip_discount = input()
days = int(input())
price = 0
total_price = 0
condition = True

if days < 1:
    print(f"Days must be positive number!")
else:
    if city in "Bansko" "Borovets":
        if days > 7:
            days -= 1
        if type_of_stay == "withEquipment":
            price = 100
            if vip_discount == "yes":
                price *= 0.90
        elif type_of_stay == "noEquipment":
            price = 80
            if vip_discount == "yes":
                price *= 0.95
        else:
            condition = False
    elif city in "Varna" "Burgas":
        if days > 7:
            days -= 1
        if type_of_stay == "withBreakfast":
            price = 130
            if vip_discount == "yes":
                price *= 0.88
        elif type_of_stay == "noBreakfast":
            price = 100
            if vip_discount == "yes":
                price *= 0.93
        else:
            condition = False
    else:
        condition = False
total_price = price * days
if not condition and days > 0:
    print(f"Invalid input!")
if condition and days > 0:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
