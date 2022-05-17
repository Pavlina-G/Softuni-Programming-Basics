party_price = float(input())
number_love_message = int(input())
number_wax_rose = int(input())
number_keychain = int(input())
number_caricature = int(input())
number_luck_surprise = int(input())

price_love_message = 0.60
price_wax_rose = 7.20
price_keychain = 3.60
price_caricature = 18.20
price_luck_surprise = 22.00

total_number = number_caricature + number_keychain + number_luck_surprise+ number_wax_rose + number_love_message
total_price = number_caricature * price_caricature + number_keychain * price_keychain + number_wax_rose * price_wax_rose\
              + number_luck_surprise * price_luck_surprise + number_love_message * price_love_message

if total_number >= 25:
    total_price *= 0.65

hosting_cost = 0.10 * total_price
total_price -= hosting_cost
difference = abs(party_price - total_price)

if total_price >= party_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")