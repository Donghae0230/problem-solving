-- 문제: N번째로 높은 Salary 찾기
-- 풀이방식: 사용자 정의 함수 사용

CREATE FUNCTION getNthHighestSalary(N INT) 
RETURNS INT
BEGIN
  RETURN (
        SELECT 
        -- CASE문 사용해서 NULL값 처리
            CASE WHEN COUNT(temp.Salary) < N THEN NULL
                ELSE MIN(temp.Salary)
            END
        FROM (
            -- Salary 중복 제거 후 정렬, N번째까지 자르기
            SELECT DISTINCT Salary
            FROM Employee
            ORDER BY Salary DESC
            LIMIT N
        ) temp  
  );
END

-- 풀이방식 2) IF (condition, value_if_ture, value_if_false)
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN 
  RETURN (
    -- IF 함수 사용
    SELECT IF(COUNT(temp.salary)=N, MIN(temp.salary), NULL)
    FROM(
        SELECT DISTINCT salary 
        FROM employee
        ORDER BY salary DESC
        LIMIT N   
    ) temp
  );
END

-- 풀이방식 3) 서브쿼리 없이 LIMIT와 OFFSET 사용
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT DISTINCT salary
        FROM employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END
