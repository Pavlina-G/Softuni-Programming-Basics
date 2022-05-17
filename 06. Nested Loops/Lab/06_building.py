# floor_number = int(input())
# room_number= int(input())
# room = ""
#
# for f in range(floor_number, 0, -1):
#     for r in range(room_number):
#         current_number_of_rooms = f * 10 + r
#         if f == floor_number:
#             print(f"L{current_number_of_rooms} ",end ="")
#         elif f % 2 != 0:
#             room += f"A{current_number_of_rooms} "
#         else:
#             room += f"O{current_number_of_rooms} "
#     print(room)
#     room = ""

floor = int(input())
room = int(input())

for f in range(floor, 0, -1):
    if f == floor or floor == 1:
        add = "L"
    elif f % 2 != 0:
        add = "A"
    else:
        add = "O"
    for r in range(room):
        print(f"{add}{f}{r} ", end="")
    print()
