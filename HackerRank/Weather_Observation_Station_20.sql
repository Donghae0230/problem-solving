-- 문제: STATION 테이블 LAT_N 컬럼의 median 구하기
-- 풀이방식: COUNT(*)를 사용해서 전체 데이터 수가 홀수인 것을 확인하고 작성
SELECT ROUND(tmp.LAT_N, 4)
FROM
    (SELECT
        row_number() over(order by LAT_N) AS num
        , LAT_N
     FROM STATION) tmp
WHERE tmp.num = 
    (SELECT COUNT(*) DIV 2 + 1
     FROM STATION)
;

-- 다른풀이 (1): 사용자 정의 변수를 사용해 데이터 수에 상관없이 median 구하기
-- SET 외의 명령어에서는 =가 비교연산자로 사용되기 때문에 값을 대입할 때에는 :=사용
SET @rownum=-1;
SELECT ROUND(AVG(LAT_N), 4)
FROM
    (SELECT 
        @rownum:=@rownum+1 AS num
        , LAT_N
     FROM STATION
     ORDER BY LAT_N) tmp
WHERE num IN (FLOOR(@rownum/2), CEIL(@rownum/2))
;

-- 다른풀이 (2): PERCENT_RANK()함수 사용하기
-- PERCENT_RANK()는 임의의 컬럼의 백분율 순위를 계산한다.
SELECT ROUND(tmp.LAT_N, 4)
FROM 
    (SELECT
        LAT_N
        , PERCENT_RANK() OVER (ORDER BY LAT_N) percent
     FROM STATION) tmp
WHERE tmp.percent = 0.5