h_cm = float(input())*100
w_cm = float(input())*100

working_place_h = 120
working_place_w = 70
hallway_w = 100
entrance_door_w = 160
department_h = 160
department_w = 120

area_no_hallway= w_cm-hallway_w
working_place_no_hallway = (area_no_hallway // working_place_w)
working_place_lenght = h_cm // working_place_h
total_working_place = (working_place_no_hallway * working_place_lenght) - 3

print (total_working_place)