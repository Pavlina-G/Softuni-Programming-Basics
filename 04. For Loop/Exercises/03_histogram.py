num = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

count_numbers = 0
for i in range(num):
    number = int(input())
    if 1 <= number < 200:
        p1 += 1
    elif number <= 399:
        p2 += 1
    elif number <= 599:
        p3 += 1
    elif number <= 799:
        p4 += 1
    elif number >= 800:
        p5 += 1
print(f"{p1 / num * 100:.2f}%")
print(f"{p2 / num * 100:.2f}%")
print(f"{p3 / num * 100:.2f}%")
print(f"{p4 / num * 100:.2f}%")
print(f"{p5 / num * 100:.2f}%")

