-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;