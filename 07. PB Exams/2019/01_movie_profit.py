movie_name = input()
days_number = int(input())
tickets_number = int(input())
ticket_price = float(input())
cinema_percent = int(input())

sum_per_day = tickets_number * ticket_price
profit_all_period = days_number * sum_per_day
percent_cinema = profit_all_period * (cinema_percent / 100)
total_profit = profit_all_period - percent_cinema
print(f"The profit from the movie {movie_name} is {total_profit:.2f} lv.")