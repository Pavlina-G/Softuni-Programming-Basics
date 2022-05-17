rent = int(input())
total_cost = 0
statuettes = rent * 0.70
catering = statuettes * 0.85
sound_system = catering / 1/2

total_cost = rent + statuettes + catering + sound_system
print(f"{total_cost:.2f}")
