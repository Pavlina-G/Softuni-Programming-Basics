target = int(input())
start_height = target - 30

failed = False
jump_counter = 0
failed_jump = 0

while not failed:

    current_height = int(input())
    jump_counter += 1

    if current_height <= start_height:
        failed_jump += 1
        if failed_jump == 3:
            failed = True
    else:
        if start_height >= target:
            break
        start_height += 5
        failed_jump = 0

if not failed:
    print(f"Tihomir succeeded, he jumped over {start_height}cm after {jump_counter} jumps.")
else:
    print(f"Tihomir failed at {start_height}cm after {jump_counter} jumps.")


