-- 문제: 각 Department에서 Salary Top 3인 직원들 찾기(중복 O)
-- 풀이방식: window function중 DENSE_RANK() 사용

SELECT
    temp.Department
    , temp.Employee
    , temp.Salary
FROM(
    SELECT 
        d.name AS Department
        , e.name AS Employee
        , e.salary AS Salary
        , DENSE_RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS Rank
    FROM Employee e
        INNER JOIN Department d ON e.departmentId=d.id 
) temp
WHERE temp.Rank < 4 
