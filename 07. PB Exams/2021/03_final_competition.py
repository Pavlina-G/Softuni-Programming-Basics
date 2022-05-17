number_of_dancers = int(input())
score = float(input())
season = input()
place = input()

# money_prize = 0
# charity_amount = 0
# money_per_dancer = 0

if place == "Bulgaria":
    money_prize = score * number_of_dancers
    if season == "summer":
        money_prize -= money_prize * 0.05
    elif season == "winter":
        money_prize -= money_prize * 0.08

elif place == "Abroad":
    money_prize = number_of_dancers * score
    money_prize *= 1.50
    if season == "summer":
        money_prize -= money_prize * 0.10
    elif season == "winter":
        money_prize -= money_prize * 0.15

charity_amount = 0.75 * money_prize
money_per_dancer = (money_prize - charity_amount) / number_of_dancers

print(f"Charity - {charity_amount:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
