WITH cnt_tbl AS (
    SELECT
        submission_date
        , COUNT(hacker_id) AS cnt
    FROM (
    SELECT
        DISTINCT hacker_id
        , submission_date
        , ROW_NUMBER () OVER (PARTITION BY hacker_id ORDER BY submission_date) - 1 AS row_num
    FROM submissions
    ) temp
    WHERE DATEDIFF(day, '2016-03-01', submission_date) = row_num
    GROUP BY submission_date
)
, rank_tbl AS (
    SELECT
        submission_date
        , hacker_id
        , ROW_NUMBER () OVER (PARTITION BY submission_date ORDER BY cnt DESC, hacker_id) AS rank
    FROM (
    SELECT
        submission_date
        , hacker_id
        , COUNT(submission_id) AS cnt
    FROM submissions
    GROUP BY
        submission_date
        , hacker_id
    ) temp
)