amount = int(input())
command = input()
average_cash = 0
average_card = 0
cash_counter = 0
card_counter = 0
payment_counter = 0
cash_paid = 0
card_paid = 0
amount_is_collected = False

while command != "End":
    price = int(command)
    payment_counter += 1
    if payment_counter % 2 != 0:
        if price > 100:
            print("Error in transaction!")
        else:
            cash_counter += 1
            print(f"Product sold!")
            cash_paid += price
    else:
        if price < 10:
            print("Error in transaction!")
        else:
            card_counter += 1
            print(f"Product sold!")
            card_paid += price
    if amount <= (card_paid + cash_paid):
        amount_is_collected = True
        break
    command = input()
if amount_is_collected:
    print(f"Average CS: {cash_paid/cash_counter:.2f}")
    print(f"Average CC: {card_paid/card_counter:.2f}")
if command == "End":
    print(f"Failed to collect required money for charity.")