player1 = input()
player2= input()
command = input()
score1 = 0
score2 = 0
game_won = False

while command != "End of game":
    card1 = int(command)
    card2 = int(input())

    if card1 > card2:
        score1 += (card1 - card2)
    elif card1 < card2:
        score2 += (card2 - card1)
    elif card1 == card2:
        print(f"Number wars!")
        card1 = int(input())
        card2 = int(input())
        if card1 > card2:
            game_won = True
            winner = player1
            win_score = score1
            break
        elif card1 < card2:
            game_won = True
            winner = player2
            win_score = score2
            break
    command = input()
if game_won:
    print(f"{winner} is winner with {win_score} points")
else:
    print(f"{player1} has {score1} points")
    print(f"{player2} has {score2} points")




