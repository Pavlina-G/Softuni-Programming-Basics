budget = float(input())
command = input()
counter = 0
total_price = 0
condition = True
while command != "Stop":
    product_name = command
    counter += 1
    product_price = float(input())
    if counter % 3 == 0:
        product_price *= 0.50
    total_price += product_price
    budget -= product_price

    if budget < 0:
        condition = False
        break
    command = input()

if condition:
    print(f"You bought {counter} products for {total_price:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {abs(budget):.2f} leva!")