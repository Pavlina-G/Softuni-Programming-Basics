result1 = input()
result2 = input()
result3 = input()
won_game = 0
lost_game = 0
drawn_game = 0

for char in (result1, result2, result3):
    if int(char[0]) > int(char[2]):
        won_game += 1
    elif int(char[0]) < int(char[2]):
        lost_game += 1
    elif int(char[0]) == int(char[2]):
        drawn_game += 1

print(f"Team won {won_game} games.")
print(f"Team lost {lost_game} games.")
print(f"Drawn games: {drawn_game}")

