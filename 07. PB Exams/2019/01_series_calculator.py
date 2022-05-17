from math import floor

name_series = input()
seasons = int(input())
episodes = int(input())
time_series = float(input())
ad_time = 0.20 * time_series
last_episode_add_time = seasons * 10

time_series += ad_time
total_time = (seasons * episodes * time_series) + last_episode_add_time
print(f"Total time needed to watch the {name_series} series is {floor(total_time)} minutes.")