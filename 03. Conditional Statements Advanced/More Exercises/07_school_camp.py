season = input()
group = input()
students_num = int(input())
nights = int(input())

price = 0
sport = ""

if season == "Winter":
    if group == "girls" or group == "boys":
        price = 9.60
        if group == "girls":
            sport = "Gymnastics"
        elif group == "boys":
            sport = "Judo"
    elif group == "mixed":
        price = 10
        sport = "Ski"
if season == "Spring":
    if group == "girls" or group == "boys":
        price = 7.20
        if group == "girls":
            sport = "Athletics"
        elif group == "boys":
            sport = "Tennis"
    elif group == "mixed":
        price = 9.50
        sport = "Cycling"
if season == "Summer":
    if group == "girls" or group == "boys":
        price = 15
        if group == "girls":
            sport = "Volleyball"
        elif group == "boys":
            sport = "Football"
    elif group == "mixed":
        price = 20
        sport = "Swimming"

total_price = students_num * price * nights

if students_num >= 50:
    total_price *= 0.50
elif 20 <= students_num:
    total_price *= 0.85
elif 10 <= students_num:
    total_price *= 0.95
print(f"{sport} {total_price:.2f} lv.")