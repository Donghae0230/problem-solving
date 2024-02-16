 SELECT 
        player_id
        , MIN(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS first_login
        , LEAD(event_date, 1, NULL) OVER (PARTITION BY player_id ORDER BY event_date) AS second_login
    FROM activity