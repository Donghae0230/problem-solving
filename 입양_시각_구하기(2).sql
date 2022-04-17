-- WITH RECURSIVE을 사용해 재귀 구현
WITH RECURSIVE hours AS (
	SELECT 0 AS hour
	UNION ALL
	SELECT hour + 1 FROM hours WHERE hour < 23
)

SELECT hours.hour, 
       CASE
            WHEN outs.count IS NULL THEN 0
            ELSE outs.count
       END AS count
FROM hours
LEFT JOIN (SELECT HOUR(DATETIME) AS hour, COUNT(*) AS count
            FROM ANIMAL_OUTS
            GROUP BY HOUR(DATETIME)
            ) outs ON hours.hour = outs.hour
ORDER BY hours.hour