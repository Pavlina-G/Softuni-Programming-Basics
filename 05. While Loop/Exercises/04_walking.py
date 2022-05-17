steps_goal = 10000
total_steps = 0
goal_reached = True

while total_steps < steps_goal:
    command = input()

    if command == "Going home":
        command = input()
        daily_steps = int(command)
        total_steps += daily_steps
        if total_steps < steps_goal:
            goal_reached = False
            print(f"{steps_goal - total_steps} more steps to reach goal.")
            break
        else:
            continue
    daily_steps = int(command)
    total_steps += daily_steps

if goal_reached:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - steps_goal} steps over the goal!")




