actor_name = input()
points = float(input())
number_of_jury = int(input())
nominee = False

for num in range(1, number_of_jury + 1):
    name_jury = input()
    score = float(input())
    points += ((len(name_jury) * score) / 2)

    if points > 1250.5:
        nominee = True
        break

difference = abs(points - 1250.5)

if nominee:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
