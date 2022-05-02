lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input()) / 100

fish_tank_volume = lenght_cm * width_cm * height_cm
fish_tank_volume_l = fish_tank_volume / 1000

water_l_needed = fish_tank_volume_l - (fish_tank_volume_l * percent)
print (water_l_needed)