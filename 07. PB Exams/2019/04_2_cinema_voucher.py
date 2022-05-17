voucher_price = int(input())
purchase = input()
tickets = 0
other = 0
price = 0

while purchase != "End":
    letter_1 = purchase[0]
    letter_2 = purchase[1]
    if len(purchase) > 8:
        price = ord(letter_1) + ord(letter_2)
    else:
        price = ord(letter_1)
    voucher_price -= price
    if voucher_price >= 0:
        if len(purchase) > 8:
            tickets += 1
        if len(purchase) <= 8 and purchase != "End":
            other += 1
    else:
        break
    purchase = input()
print(tickets)
print(other)

