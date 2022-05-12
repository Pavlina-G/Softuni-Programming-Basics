juniors = int(input())
seniors = int(input())
type_of_route = input()

fee_junior = 0.00
fee_senior = 0.00
total_money = 0.00

if juniors > 0 or seniors > 0:
    if type_of_route == "trail":
        fee_junior = 5.50
        fee_senior = 7
    elif type_of_route == "cross-country":
        fee_junior = 8
        fee_senior = 9.50
        if (juniors + seniors) >= 50:
            fee_junior *= 0.75
            fee_senior *= 0.75
    elif type_of_route == "downhill":
        fee_junior = 12.25
        fee_senior = 13.75
    elif type_of_route == "road":
        fee_junior = 20
        fee_senior = 21.50

total_money = juniors * fee_junior + seniors * fee_senior
total_money *= 0.95

print(f'{total_money:.2f}')


