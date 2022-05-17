airline = input()
ticket = int(input())
kids_ticket = int(input())
net_price_ticket = float(input())
service_fee = float(input())

kids_price_ticket = net_price_ticket * 0.30 + service_fee
net_price_ticket = net_price_ticket + service_fee
profit = ticket * net_price_ticket + kids_ticket * kids_price_ticket
profit *= 0.20
print(f"The profit of your agency from {airline} tickets is {profit:.2f} lv.")