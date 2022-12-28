-- 문제: 2019년에 거래한 buyer의 id, join date, order 수 찾기
-- 풀이방식: Left Join 사용

SELECT 
    u.user_id AS buyer_id
    , u.join_date
    , CASE
        WHEN o.cnt THEN o.cnt 
        ELSE 0
    END AS orders_in_2019 
FROM users u
LEFT JOIN (
    SELECT 
        buyer_id
        , COUNT(item_id) AS cnt
    FROM orders
    WHERE order_date >= '2019-01-01'
    GROUP BY buyer_id
) o ON u.user_id = o.buyer_id