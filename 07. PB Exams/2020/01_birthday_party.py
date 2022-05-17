rent = float(input())
price_cake = 0
price_drinks = 0
price_animator = 0

price_cake = 0.20 * rent
price_drinks = price_cake - (price_cake * 0.45)
price_animator = rent * 1/3

budget = rent + price_drinks + price_cake + price_animator
print(budget)
