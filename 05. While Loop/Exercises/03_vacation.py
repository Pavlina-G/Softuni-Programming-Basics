needed_money = float(input())
available_money = float(input())

day_counter = 0
spending_counter = 0

while available_money < needed_money and spending_counter < 5:
    action_type = input()
    amount = float(input())
    day_counter += 1

    if action_type == "spend":
        available_money -= amount
        spending_counter += 1 #days of spending
        if available_money < 0:
            available_money = 0
    if action_type == "save":
        available_money += amount
        spending_counter = 0  # nulira broyacha

if spending_counter == 5:
    print(f"You can't save the money.")
    print(f"{day_counter}")
if available_money >= needed_money:
    print(f"You saved the money for {day_counter} days.")

