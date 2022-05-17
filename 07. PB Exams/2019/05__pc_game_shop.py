sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0


for game in range(sold_games):
    game = input()
    if game == "Hearthstone":
        hearthstone += 1
    elif game == "Fornite":
        fornite += 1
    elif game == "Overwatch":
        overwatch += 1
percent_h = hearthstone / sold_games * 100
percent_f = fornite / sold_games * 100
percent_o = overwatch / sold_games * 100
percent_others = 100 - (percent_o + percent_f + percent_h)

print(f"Hearthstone - {percent_h:.2f}%")
print(f"Fornite - {percent_f:.2f}%")
print(f"Overwatch - {percent_o:.2f}%")
print(f"Others - {percent_others:.2f}%")

