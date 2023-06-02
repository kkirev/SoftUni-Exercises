"""
https://judge.softuni.org/Contests/Practice/Index/1699#9

Петък вечер е и се чудите кой филм да си пуснете да гледате. Решавате да напишете програма, която да избере това вместо
вас. До команда "STOP" получавате заглавия на любими ваши филми. Най-добрият филм за вас ще бъде този,
който има най-много точки. Точките се изчисляват като сбор от ASCII стойностите на символите в заглавието на филма
(няма да има случай, в който имаме два филма с равен брой точки).
При изчислението на точките трябва да се има предвид следното:
•	За всяка малка буква в заглавието, от сумата трябва да се извади два пъти дължината на заглавието на филма.
•	За всяка главна буква в заглавието, от сумата трябва да се извади дължината на заглавието на филма.
Може да имате максимум 7 заглавия на филми.

Вход
От конзолата се четат редове до команда "STOP" или до достигането на лимита от 7 филма:
•	Заглавие на филм  – текст;

Изход
На конзолата да се отпечата:
•	Ако сте достигнали лимита от 7 филма трябва да отпечатате:
"The limit is reached."
Да се отпечата най-добрият филм за вас:
"The best movie for you is {заглавие на филм} with {сума на символите} ASCII sum."
"""

user_input = input()
movie_counter = 0
movie_points = 0
favorite_movie_points = 0
limit_reached = False

while user_input != 'STOP':
    movie_counter += 1

    if movie_points > favorite_movie_points:
        favorite_movie_points = movie_points
        favorite_movie = movie_name

    if movie_counter == 7:
        limit_reached = True
        break

    movie_name = user_input
    movie_points = 0

    for letter in range(len(movie_name)):
        if 65 <= ord(str(movie_name[letter])) <= 90:
            movie_points += ord(str(movie_name[letter])) - len(movie_name)
        elif 97 <= ord(str(movie_name[letter])) <= 122:
            movie_points += ord(str(movie_name[letter])) - (2 * len(movie_name))
        else:
            movie_points += ord(str(movie_name[letter]))

    user_input = input()

if limit_reached:
    print(f'The limit is reached.')

print(f'The best movie for you is {favorite_movie} with {favorite_movie_points} ASCII sum.')