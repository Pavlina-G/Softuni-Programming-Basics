number_of_pens = int (input())
number_of_markers = int (input())
liters_of_detergent = int (input())
discount_percent = int (input())

pen_price = 5.80
marker_price = 7.20
liter_detergent_price = 1.20

needed_sum = (number_of_pens * pen_price) + \
             (number_of_markers * marker_price) + \
             (liters_of_detergent * liter_detergent_price)
             
# discount_percent = discount_percent/100
# discount_percent /= 100

total_sum = needed_sum - (needed_sum * discount_percent /100)
print (total_sum)
