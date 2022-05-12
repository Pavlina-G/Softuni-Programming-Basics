import sys

number = int(input())
sum_num = 0
max_num = -sys.maxsize

for i in range(number):
    num = int(input())
    sum_num += num
    if num > max_num:
        max_num = num
if max_num == sum_num - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    difference = abs(max_num - (sum_num -max_num))
    print(f"No")
    print(f"Diff = {difference}")
