player = input()
goal = 0
hat_trick = False
max_goal = 0
best_player = ""
while player != "END":
    goal = int(input())
    if goal > max_goal:
        max_goal = goal
        best_player = player
    if goal >= 3:
        hat_trick = True
    if goal >= 10:
        break
    player = input()
print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {max_goal} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goal} goals.")

