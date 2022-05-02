annual_fee = int(input())

basketball_shoes = annual_fee - annual_fee * 0.4
basketball_clothes = basketball_shoes - 0.2 * basketball_shoes
basketball = 1 / 4 * basketball_clothes
basketball_accessories = 1 / 5 * basketball

total_price = annual_fee + basketball_accessories + basketball \
              + basketball_clothes + basketball_shoes
print (total_price)