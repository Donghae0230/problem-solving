-- 문제: 3번 이상 연속되는 num 찾기
-- 풀이방식: window function중 LAG()를 사용

SELECT DISTINCT(afternext) AS ConsecutiveNums
FROM(
    SELECT 
        num
        , LAG(num, 1) OVER (ORDER BY id) AS next
        , LAG(num, 2) OVER (ORDER BY id) AS afternext
    FROM LOGS
) temp 
WHERE temp.num=temp.next 
    AND temp.next=temp.afternext