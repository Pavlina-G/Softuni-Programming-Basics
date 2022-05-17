counter = 0
max_points = 0
movie_name = input()

while movie_name != "STOP":
    total_points = 0
    points = 0
    counter += 1

    if counter > 7:
        break

    if counter == 7:
        print(f"The limit is reached.")
        break

    for char in movie_name:
        points = 0
        if char.islower():
            points = (ord(char) - (2 * len(movie_name)))
        elif char.isupper():
            points = (ord(char)) - len(movie_name)
        else:
            points = ord(char)
        total_points += points

    if total_points > max_points:
        max_points = total_points
        the_best_movie = movie_name

    movie_name = input()

print(f"The best movie for you is {the_best_movie} with {max_points} ASCII sum.")
