-- make query
SELECT tv_genres.name AS genre,
count(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id=tv_show_genres.genre_id
WHERE tv_show_genres.genre_id is not null
GROUP BY genre
ORDER BY number_of_shows DESC;
