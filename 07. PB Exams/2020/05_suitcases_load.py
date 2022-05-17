capacity = float(input())
command = input()
counter_suitcase = 0
plane_is_full = False

while command != "End":
    volume_suitcase = float(command)
    if (counter_suitcase + 1) % 3 == 0:
        volume_suitcase *= 1.10
    capacity -= volume_suitcase
    if capacity < 0:
        plane_is_full = True
        break
    counter_suitcase += 1
    command = input()

if command == "End":
    print(f"Congratulations! All suitcases are loaded!")
if plane_is_full:
    print(f"No more space!")
print(f"Statistic: {counter_suitcase} suitcases loaded.")
