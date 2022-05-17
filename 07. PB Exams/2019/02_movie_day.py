time_for_acting = int(input())
number_scenes = int(input())
time_for_scene = int(input())
starting_time = 0.15 * time_for_acting

total_time = starting_time + number_scenes * time_for_scene
difference = abs(total_time - time_for_acting)

if total_time <= time_for_acting:
    print(f"You managed to finish the movie on time! You have {difference:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {difference:.0f} minutes.")