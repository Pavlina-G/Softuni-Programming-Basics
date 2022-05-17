a1 = int(input())
a2 = int(input())
n = int(input())

for num1 in range(a1, a2):
    for num2 in range(1, n):
        for num3 in range(1, int(n / 2)):
            for num4 in (chr(num1)):
                if num1 % 2 != 0:
                    if (num2 + num3 + ord(num4)) % 2 != 0:
                        print(f"{chr(num1)}-{num2}{num3}{ord(num4)}")
