-- Lists all cities contained in the database hbtn_0d_usa
-- Results are sorted in ascending order by cities.id
-- Uses only one SELECT statement
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;