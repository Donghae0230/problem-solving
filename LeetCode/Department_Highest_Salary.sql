-- 문제: 각 Department에서 가장 높은 급여를 받는 직원 찾기
-- 풀이방식: window function중 MAX() 사용

SELECT 
    temp.Department
    , temp.Employee
    , temp.Salary
FROM (
    SELECT d.name AS Department
        , e.name AS Employee
        , e.salary AS Salary
        , MAX(e.salary) OVER (PARTITION BY d.id) AS HighestSalary 
    FROM Employee e
        INNER JOIN Department d ON e.departmentId = d.id
) temp
WHERE temp.Salary = temp.HighestSalary