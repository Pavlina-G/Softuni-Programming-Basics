first_number = input()
second_number = input()

for num1 in range(int(first_number[0]), int(second_number[0]) + 1):
    for num2 in range(int(first_number[1]), int(second_number[1]) + 1):
        for num3 in range(int(first_number[2]), int(second_number[2]) + 1):
            for num4 in range(int(first_number[3]), int(second_number[3]) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f"{num1}{num2}{num3}{num4}")









# m = (input())
# n = (input())
#
# counter = 0
# for i in m:
#
#     if counter == 0:
#         a = int(i)
#     elif counter == 1:
#         b = int(i)
#     elif counter == 2:
#         c = int(i)
#     elif counter == 3:
#         d = int(i)
#     counter += 1
# counter = 0
# for i in n:
#
#     if counter == 0:
#         a1 = int(i)
#     elif counter == 1:
#         b1 = int(i)
#     elif counter == 2:
#         c1 = int(i)
#     elif counter == 3:
#         d1 = int(i)
#     counter += 1
# for i in range(a, a1 + 1):
#     for j in range(b, b1 + 1):
#         for k in range(c, c1 + 1):
#             for l in range(d, d1 + 1):
#                 if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
#                     print(f"{i}{j}{k}{l}", end =" ")