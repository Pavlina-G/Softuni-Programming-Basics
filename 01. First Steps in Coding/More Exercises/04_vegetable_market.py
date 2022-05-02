price_veg_kg = float(input())
price_fruits_kg = float(input())
kg_veg = int(input())
kg_fruits = int(input())

income_bgn = (price_veg_kg * kg_veg) + (price_fruits_kg * kg_fruits)
income_eur= income_bgn/ 1.94
print('%.2f' %(income_eur))
