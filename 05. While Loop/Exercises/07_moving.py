weight_apartment = int(input())
lenght_apartment = int(input())
height_apartment = int(input())
command = input()
volume_apartment = weight_apartment * lenght_apartment * height_apartment
volume_box = 0
place_is_full = False

while command != "Done": #and volume_apartment >= 0
    box_counter = int(command)
    volume_apartment -= box_counter
    if volume_apartment < 0:
        place_is_full = True
        break
    command = input()
if place_is_full:
    print(f"No more free space! You need {abs(volume_apartment)} Cubic meters more.")
else:
    print(f"{volume_apartment} Cubic meters left.")
