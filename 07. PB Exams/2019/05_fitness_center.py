people = int(input())
back = 0
chest = 0
legs = 0
abs = 0
shake = 0
bar = 0

for man in range(1, people + 1):
    activity = input()

    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        shake += 1
    elif activity == "Protein bar":
        bar += 1

buyers_counter = shake + bar
workout_counter = back + chest + legs + abs

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{workout_counter / people * 100:.2f}% - work out")
print(f"{buyers_counter /people * 100:.2f}% - protein")
