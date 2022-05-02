nylon_sq_m = int(input())
paint_l = int(input())
painting_diluent_l= int(input())
hours_for_work = int(input())

nylon_sq_m_price = 1.50
paint_l_price = 14.50
painting_diluent_l_price= 5.00

nylon_cost = (nylon_sq_m + 2) * nylon_sq_m_price
paint_cost = (paint_l + paint_l * 0.1) * paint_l_price
painting_diluent_l_cost = painting_diluent_l * painting_diluent_l_price
other_cost = 0.40

total_material_cost = nylon_cost + paint_cost + painting_diluent_l_cost + other_cost
workers_cost = (total_material_cost * 30 / 100) * 8

total_cost = total_material_cost + workers_cost
print(total_cost)
