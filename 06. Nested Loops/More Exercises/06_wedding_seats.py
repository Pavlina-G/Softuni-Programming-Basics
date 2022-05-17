last_sector = input()
first_sector = "A"
rows_first_sector = int(input())
odd_seats = int(input())
start_seat = ord("a")
total_seats = 0
sector_counter = 0

for sector in range(ord(first_sector),ord(last_sector) + 1):
    sector_counter += 1
    if sector_counter > 1:
        rows_first_sector += 1
    for row in range(1, rows_first_sector + 1):
        if row % 2 != 0:
            for seat in range(start_seat, (start_seat + odd_seats)):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
        elif row % 2 == 0:
            for seat in range(start_seat, (start_seat + odd_seats + 2)):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
print(total_seats)

