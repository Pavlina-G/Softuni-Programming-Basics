budget = float(input())

while True:
    command = input()
    actor = command

    if command == "ACTION":
        break

    if len(actor) <= 15:
        price = float(input())

    if len(actor) > 15:
        budget = budget - (0.20 * budget)
    else:
        budget -= price

    if budget <= 0:
        break

if budget >= 0:
    print(f"We are left with {abs(budget):.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")


