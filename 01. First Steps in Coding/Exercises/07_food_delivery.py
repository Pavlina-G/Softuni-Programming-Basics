chicken_menu = int(input())
fish_menu = int(input())
vegetаrian_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetаrian_menu_price = 8.15
delivery_price = 2.50

total_bill_without_delivery = chicken_menu_price * chicken_menu + \
                              fish_menu_price * fish_menu + \
                              vegetаrian_menu_price * vegetаrian_menu

desert_price = 20 /100 * total_bill_without_delivery
total_bill = total_bill_without_delivery + desert_price + delivery_price
print (total_bill)