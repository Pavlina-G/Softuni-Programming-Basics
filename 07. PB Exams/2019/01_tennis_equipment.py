from math import floor, ceil

price_racket = float(input())
number_tennis_racket = int(input())
number_sneakers = int(input())

price_sneakers = 1/6 * price_racket

total_price = number_tennis_racket * price_racket+ number_sneakers * price_sneakers
total_price *= 1.20

sponsor_price = 7/8 * total_price
total_price -= sponsor_price

print(f"Price to be paid by Djokovic {floor(total_price)}")
print(f"Price to be paid by sponsors {ceil(sponsor_price)}")
