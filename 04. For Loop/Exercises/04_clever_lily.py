# age = int(input())
# washing_machine_price = float(input())
# toy_price = int(input())
# toy_number = 0
# money = 10
# saved_money = 0
# for i in range(1,age+1):
#     if i % 2 != 0:
#         toy_number += 1
#         toy_money = toy_number * toy_price
#     else:
#         saved_money += money - 1
#         money += 10
#
# saved_money = saved_money + toy_money
# difference = abs(saved_money- washing_machine_price)
# if saved_money >= washing_machine_price:
#     print(f"Yes! {difference:.2f}")
# else:
#     print(f"No! {difference:.2f}")

# Other way:
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
total_money = 0
total_toys = 0
birthday_money = 0

for current_age in range (1, age + 1):
    if current_age % 2 != 0:
        total_toys += 1
    else:
        birthday_money += 10
        total_money += birthday_money - 1
total_money += total_toys * toy_price
difference = abs(total_money - washing_machine_price)
if total_money >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")