movie_number = int(input())

the_best_movie = ""
the_worst_movie = ""
max_rate = -9999999999999
min_rate = 9999999999999
average_rating = 0

for movie in range(movie_number):
    movie_name = input()
    rating = float(input())
    average_rating += rating
    if rating > max_rate:
        max_rate = rating
        the_best_movie = movie_name
    if rating < min_rate:
        min_rate = rating
        the_worst_movie = movie_name

print(f"{the_best_movie} is with highest rating: {max_rate:.1f}")
print(f"{the_worst_movie} is with lowest rating: {min_rate:.1f}")
print(f"Average rating: {average_rating/movie_number:.1f}")
