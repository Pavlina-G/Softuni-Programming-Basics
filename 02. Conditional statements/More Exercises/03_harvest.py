from math import floor, ceil

x_m2_vineyard = int(input())
y_grapes_m2 = float(input())
z_needed_wine_l = int(input())
number_of_workers = int(input())

grapes = x_m2_vineyard * y_grapes_m2
wine = 0.4 * grapes / 2.5
difference = abs(wine-z_needed_wine_l)

if wine < z_needed_wine_l:
    print(f'It will be a tough winter! More {floor(difference)} liters wine needed.')
else:
    left_wine = difference/number_of_workers
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(difference)} liters left -> {ceil(left_wine)} liters per person.')


