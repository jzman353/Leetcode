"""
1341. Movie Rating
Solved
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Movies

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.

Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.

Table: MovieRating

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date.

Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
The result format is in the following example.

Example 1:

Input:
Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  |
| 2           | 2            | 2            | 2020-02-01  |
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  |
| 3           | 2            | 4            | 2020-02-25  |
+-------------+--------------+--------------+-------------+
Output:
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
Explanation:
Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.
"""
#92%

import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    c = collections.Counter(list(movie_rating['user_id']))
    maxx = c.most_common()[0][1]
    s = set()
    for i in c.most_common():
        if i[1] != maxx:
            break
        s.add(i[0])
    users = users[users['user_id'].isin(s)]
    user = min(users['name'])

    df = movie_rating.loc[(movie_rating['created_at'] >= '2020-02-01') & (movie_rating['created_at'] < '2020-03-01')]
    df = df.groupby('movie_id')['rating'].mean().reset_index()
    max_rating = max(df['rating'])
    df = df[df['rating'] == max_rating]
    s = set(df['movie_id'])
    movies = movies[movies['movie_id'].isin(s)]
    movie = min(movies['title'])

    return pd.DataFrame({"results": [user, movie]})

"""
import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    movie_rating = movie_rating.merge(movies,how = 'left',on = 'movie_id')
    movie_rating = movie_rating.merge(users,how = 'left',on = 'user_id')

    most_rating_guy = movie_rating[movie_rating['name'] == movie_rating.sort_values(by = 'name')['name'].value_counts().idxmax()]['name'].drop_duplicates(keep = 'first')

    best_rated_movie = movie_rating[(movie_rating['created_at'].dt.month == 2) & (movie_rating['created_at'].dt.year == 2020)].sort_values(by = 'title')
    best_rated_movie = best_rated_movie[best_rated_movie['title'] == best_rated_movie.groupby('title')['rating'].mean().idxmax()]['title'].drop_duplicates(keep = 'first')
    

    mocnhien = pd.concat([pd.DataFrame(columns = ['results']),pd.DataFrame(pd.Series([*most_rating_guy,*best_rated_movie]),columns = ['results'])],ignore_index = True)
    return mocnhien
"""