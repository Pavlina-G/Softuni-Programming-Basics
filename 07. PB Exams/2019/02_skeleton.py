control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds_per_100m = int(input())

control_seconds += (control_minutes * 60)
cut_time = length / 120 * 2.5
current_time = (length / 100 * seconds_per_100m) - cut_time

if current_time <= control_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {current_time:.3f}.")
else:
    difference = abs(current_time - control_seconds)
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
