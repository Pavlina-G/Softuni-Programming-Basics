strawberry_price = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())

raspberry_price = 0.50 * strawberry_price
orange_price = raspberry_price - (0.4 * raspberry_price)
banana_price = raspberry_price - (0.8 * raspberry_price)

total_amount = strawberry_kg * strawberry_price + raspberry_price * raspberry_kg + \
               banana_price * banana_kg + orange_price * orange_kg
print(f"{total_amount:.2f}")