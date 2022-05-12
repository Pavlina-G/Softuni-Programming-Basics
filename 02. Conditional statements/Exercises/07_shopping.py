budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

price_videocard = 250
price_processor = 0.35 * price_videocard * video_cards
price_ram = 0.1 * price_videocard * video_cards
cost = (video_cards * price_videocard) + (processors * price_processor) + \
       (ram * price_ram)
if video_cards > processors:
    cost *= 0.85
difference = abs(budget - cost)
if cost > budget:
    print(f"Not enough money! You need {difference:.2f} leva more!")
else:
    print(f"You have {difference:.2f} leva left!")

