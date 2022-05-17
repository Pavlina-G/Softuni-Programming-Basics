most_powerful_word = ""
most_powerful_word_score = 0

while True:
    word = input()

    if word == "End of words":
        break

    current_counter_of_chars = 0

    for char in word:
        print(char)
        current_counter_of_chars += ord(char)

    if word[0].lower() in "aeiouy":
        current_counter_of_chars = current_counter_of_chars * len(word)
    else:
        current_counter_of_chars = int(current_counter_of_chars / len(word))

    if current_counter_of_chars > most_powerful_word_score:
        most_powerful_word = word
        most_powerful_word_score = current_counter_of_chars

print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_score}")

# command = input()
# the_best_word = ""
# the_best = 0
#
#
# while command != "End of words":
#     sum_ascii_word = 0
#     word = str(command)
#     first_letter = ord(word[0])
#     for index,digit in enumerate(word):
#         sum_ascii_word += ord(digit)
#         if chr(first_letter) == "a" or chr(first_letter) == "e" or chr(first_letter) == "i" or chr(first_letter) == "o" or chr(first_letter) == "u" or chr(first_letter) == "y" or \
#                 chr(first_letter) == "A" or chr(first_letter) == "E" or chr(first_letter) == "I" or chr(first_letter) == "O" or chr(first_letter) == "U" or chr(first_letter) == "Y":
#             total_sum = sum_ascii_word * len(word)
#         else:
#             total_sum = int(sum_ascii_word / len(word))
#     if total_sum > the_best:
#         the_best = total_sum
#         the_best_word = word
#     command = input()
# print(f"The most powerful word is {the_best_word} - {the_best}")