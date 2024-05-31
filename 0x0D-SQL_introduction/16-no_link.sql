-- lists all records of the table arranged in descending order
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
