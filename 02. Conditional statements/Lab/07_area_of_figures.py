from math import pi

figure = input()
if figure == 'circle':
    radius = float(input())
    area = pi * radius * radius
    print (f'{area:.3f}')
elif figure == 'square':
    a = float(input())
    area = a * a
    print(f'{area:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f'{area:.3f}')

#
from math import pi

figure = input()
if figure == 'circle':
    radius = float(input())
    area = pi * radius ** 2
    print (f'{area:.3f}')
elif figure == 'square':
    a = float(input())
    area = a * a
    print(f'{area:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f'{area:.3f}')

