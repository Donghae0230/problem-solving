/*
SELECT HOST_ID
FROM places
GROUP BY host_id
HAVING count(*) >= 2 
*/
SELECT *
FROM places
WHERE host_id IN (
    SELECT HOST_ID
    FROM places
    GROUP BY host_id
    HAVING count(*) >= 2 
)
ORDER BY id;