-- DATEDIFF를 사용해 두 날짜 사이 기간 구하기
SELECT ins.animal_id,
       ins.name
--     DATEDIFF(outs.datetime, ins.datetime) as date_diff
FROM animal_ins AS ins
    INNER JOIN animal_outs AS outs
    ON ins.animal_id = outs.animal_id
ORDER BY DATEDIFF(outs.datetime, ins.datetime) DESC 
LIMIT 2