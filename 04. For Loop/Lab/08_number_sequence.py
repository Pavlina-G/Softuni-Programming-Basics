import sys
# number = int(input())
# list1 = []
#
# for _ in range(number):
#     current_num = int(input())
#     list1.append(current_num)
# print("Max number:", max(list1))
# print("Min number:", min(list1))
number = int(input())
min_number = sys.maxsize#922337203
max_number = -sys.maxsize#-922337203...
for _ in range(number):
    current_num = int(input())
# print(min_number)
# print(max_number)
    if current_num > max_number:
        max_number = current_num
    if current_num < min_number:
        min_number = current_num
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
