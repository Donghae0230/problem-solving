-- 문제: Write a query to print total number of unique hackers who made at least  submission each day (starting on the first day of the contest)
--       , and find the hacker_id and name of the hacker who made maximum number of submissions each day. 
-- 풀이방식: 임시 테이블을 만들기 위해 WITH 사용. 매일 제출한 사람 수 테이블(cnt_tbl)과 제출한 사람 순위 테이블(rank_tbl)을 각각 만들어 JOIN 


WITH cnt_tbl AS (
    SELECT 
        submission_date
        , COUNT(hacker_id) AS cnt
    FROM (
        SELECT
            hacker_id
            , submission_date
            , ROW_NUMBER () OVER (PARTITION BY hacker_id ORDER BY submission_date) - 1 AS row_num
        FROM (
            SELECT 
                submission_date
                , hacker_id
                , COUNT(submission_id) AS submission_cnt
            FROM submissions
            GROUP BY 
                submission_date
                , hacker_id
        ) AS s1
    ) s2
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
    ) s
)
SELECT
    cnt_tbl.submission_date
    , cnt_tbl.cnt
    , rank_tbl.hacker_id
    , hackers.name
FROM cnt_tbl
LEFT JOIN rank_tbl
    ON cnt_tbl.submission_date = rank_tbl.submission_date
LEFT JOIN hackers
    ON rank_tbl.hacker_id = hackers.hacker_id
WHERE rank_tbl.rank = 1