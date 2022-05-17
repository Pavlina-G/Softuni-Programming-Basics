width = int(input())
height = int(input())
total_pieces = width * height
command = input()
no_more_cake = False
while command != "STOP":
    pieces_cake = int(command)
    total_pieces -= pieces_cake
    if total_pieces < 0:
        no_more_cake = True
        break
    command = input()
if no_more_cake:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")