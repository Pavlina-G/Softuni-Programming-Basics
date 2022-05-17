# command = input()
# min_num = 99999999999999
# 
# while command != "Stop":
#     number = int(command)
#     if number < min_num:
#         min_num = number
#     command = input()
# print(min_num)

min_num = 99999999999999

while True:
    number = input()
    if number == "Stop":
        break
    elif int(number) < min_num:
        min_num = int(number)

print(min_num)