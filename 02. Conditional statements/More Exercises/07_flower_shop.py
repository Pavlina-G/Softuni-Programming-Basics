from math import floor, ceil

magnolia = int(input())
hyacinth = int(input())
rose = int(input())
cactus = int(input())
gift_price = float(input())

profit = 0
magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.5
cactus_price = 8

profit = magnolia_price * magnolia + hyacinth_price * hyacinth + \
         rose_price * rose + cactus_price * cactus
profit *= 0.95
difference =abs(profit - gift_price)

if profit >= gift_price:
    print(f'She is left with {floor(difference)} leva.')
else:
    print(f'She will have to borrow {ceil(difference)} leva.')
