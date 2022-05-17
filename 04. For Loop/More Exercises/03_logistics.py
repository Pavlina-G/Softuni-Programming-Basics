cargo_number = int(input())
minibus = 0
truck = 0
train =0
average_price = 0
total_tons = 0

for cargo in range(1,cargo_number + 1):
    cargo_ton = int(input())
    if 1 <= cargo_ton <= 3:
        minibus += cargo_ton
    elif 4 <= cargo_ton <= 11:
        truck += cargo_ton
    else:
        train += cargo_ton

total_tons = minibus + truck + train
average_price = (minibus * 200 + truck* 175 + train * 120) / total_tons
print(f'{average_price:.2f}')
percent_minibus = minibus / total_tons * 100
percent_truck = truck * 100 / total_tons
percent_train = train * 100 / total_tons
print(f"{percent_minibus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")


