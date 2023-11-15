-- script 19
-- script that _displays the top 3 of _citie temp during _July and
-- _August ordered by _temp (descending).
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
