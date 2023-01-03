-- 문제: Write a query to output the names of those students whose best friends got offered a higher salary than them.
-- 풀이방식: 가장 큰 범위의 contest 테이블에서부터 LEFT JOIN 

SELECT 
    c.contest_id
    , c.hacker_id
    , c.name
    , SUM(s.sum_of_tot_sub)
    , SUM(s.sum_of_acpt_sub)
    , SUM(v.sum_of_tot_view)
    , SUM(v.sum_of_uniq_view)
FROM contests c 
LEFT JOIN colleges co
    ON c.contest_id = co.contest_id
LEFT JOIN challenges ch
    ON co.college_id = ch.college_id
LEFT JOIN (
    SELECT
        challenge_id
        , SUM(total_submissions) AS sum_of_tot_sub
        , SUM(total_accepted_submissions) AS sum_of_acpt_sub
    FROM submission_stats
    GROUP BY challenge_id
) s
    ON ch.challenge_id = s.challenge_id
LEFT JOIN (
    SELECT
        challenge_id
        , SUM(total_views) AS sum_of_tot_view
        , SUM(total_unique_views) AS sum_of_uniq_view
    FROM view_stats 
    GROUP BY challenge_id
) v 
    ON ch.challenge_id = v.challenge_id
GROUP BY c.contest_id, c.hacker_id, c.name
HAVING SUM(
    s.sum_of_tot_sub
    + s.sum_of_acpt_sub
    + v.sum_of_tot_view
    + v.sum_of_uniq_view
) != 0
ORDER BY c.contest_id;