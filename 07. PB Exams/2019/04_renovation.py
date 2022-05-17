from math import ceil

height = int(input())
width = int(input())
walls_area = (height * width) * 4
not_paint_walls = int(input())
area_for_painting = ceil(walls_area - (walls_area * not_paint_walls / 100))
command = input()

while command != "Tired!":
    paint_l = int(command)
    area_for_painting -= paint_l
    if area_for_painting <= 0:
        break
    command = input()
if command == "Tired!":
    print(f"{abs(area_for_painting)} quadratic m left.")
if area_for_painting < 0:
    print(f"All walls are painted and you have {abs(area_for_painting)} l paint left!")
if area_for_painting == 0:
    print(f"All walls are painted! Great job, Pesho!")
