numbers = int(input())
p1 = 0
p2 = 0
p3 = 0

for number in range(1, numbers + 1):
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1

percent_p1 = p1 / numbers * 100
percent_p2 = p2 / numbers * 100
percent_p3 = p3 / numbers * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
