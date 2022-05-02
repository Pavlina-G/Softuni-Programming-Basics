height_house = float(input())
lenght_side_wall = float(input())
height_roof_triangular = float(input())

front_back_wall =( 2 * height_house * height_house ) - (1.2 * 2)
side_walls = (2 * height_house * lenght_side_wall) - (2 * 1.5 * 1.5)
all_walls = front_back_wall + side_walls
green_paint = all_walls / 3.4

roof_area = 2 * (height_house * lenght_side_wall)
roof_tr_area = 2 * height_house * height_roof_triangular / 2
total_roof_area = roof_area + roof_tr_area
red_paint = total_roof_area / 4.3
print('%.2f' %(green_paint))
print('%.2f' %(red_paint))