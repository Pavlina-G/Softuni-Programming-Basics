m = int(input())
n = int(input())
start = str(m)
end = str(n)

counter = 0
for i in start:
    if counter == 0:
        a = int(i)
    elif counter == 1:
        b = int(i)
    elif counter == 2:
        c = int(i)
    elif counter == 3:
        d = int(i)
    counter += 1
counter = 0
for j in end:
    if counter == 0:
        a1 = int(j)
    elif counter == 1:
        b1 = int(j)
    elif counter == 2:
        c1 = int(j)
    elif counter == 3:
        d1 = int(j)
    counter += 1
for num1 in range(a, a1 + 1):
    for num2 in range(b, b1 + 1):
        for num3 in range(c, c1 + 1):
            for num4 in range(d, d1 + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f"{num1}{num2}{num3}{num4}", end =" ")

# m = (input())
# n = (input())
#
# count = 0
# for i in m:
#     if count == 0:
#         a = int(i)
#     elif count == 1:
#         b = int(i)
#     elif count == 2:
#         c = int(i)
#     else:
#         d = int(i)
#     count += 1
# count = 0
# for i in n:
#     if count == 0:
#         a1 = int(i)
#     elif count == 1:
#         b1 = int(i)
#     elif count == 2:
#         c1 = int(i)
#     else:
#         d1 = int(i)
#     count += 1
# for i in range(a, a1 + 1):
#     for j in range(b, b1 + 1):
#         for k in range(c, c1 + 1):
#             for l in range(d, d1 + 1):
#                 if not i % 2 == 0 and not j % 2 == 0 and not k % 2 == 0 and not l % 2 == 0:
#                     print(f'{i}{j}{k}{l} ', end='')
