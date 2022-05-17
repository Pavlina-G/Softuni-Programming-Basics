fruit = input()
set_size = input()
ordered_set = int(input())

price = 0
if fruit == "Watermelon":
    if set_size == "small":
        price = 56 * 2
    elif set_size == "big":
        price = 28.70 * 5
elif fruit == "Mango":
    if set_size == "small":
        price = 36.66 * 2
    elif set_size == "big":
        price = 19.60 * 5
elif fruit == "Pineapple":
    if set_size == "small":
        price = 42.10 * 2
    elif set_size == "big":
        price = 24.80 * 5
elif fruit == "Raspberry":
    if set_size == "small":
        price = 20 * 2
    elif set_size == "big":
        price = 15.20 * 5
total_price = ordered_set * price

if 400 <= total_price <= 1000:
    total_price *= 0.85
if total_price > 1000:
    total_price *= 0.50

print(f"{total_price:.2f} lv.")

