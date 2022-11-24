-- 문제: STATION 테이블 a, i, o, u, e로 끝나는 CITY 중복없이 출력
-- 풀이방식: LIKE를 사용하려다 너무 길어질 것 같아서 REGEXP 정규표현식 사용
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP 'a$|e$|i$|o$|u$';
-- WHERE CITY REGEXP '[aioue]$' 처럼 사용가능

-- 정규표현식 사용
-- .: 문자 하나
-- *: 앞 문자 0개 이상 반복
-- ^: 시작하는 문자열('^시작')
-- $: 끝나는 문자열('끝$')
-- []: 패턴 (예) [abc]는 abc 중 하나)
-- |: or