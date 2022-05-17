months_number = int(input())
total_bill = 0
average_monthly_bill = 0
electricity = 0
water = 0
internet = 0
other_bill = 0
for month in range(months_number):
    electricity_month = float(input())
    electricity += electricity_month
    water += 20
    internet += 15
    other_bill +=((electricity_month + 20 + 15) * 1.20)
total_bill += electricity + water + internet + other_bill
average_monthly_bill = total_bill / months_number
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {average_monthly_bill:.2f} lv")
