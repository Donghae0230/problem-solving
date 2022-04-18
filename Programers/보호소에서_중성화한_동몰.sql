/*
1) INNER JOIN 사용해서 입양된 동물 찾기
2) WHERE LIKE 사용해서 입양 전, 후 중성화 여부 찾기
3) ORDER BY 사용해서 정렬
*/
SELECT ins.animal_id AS id,
       ins.animal_type,
       ins.name
FROM animal_ins AS ins
    INNER JOIN animal_outs AS outs
    ON ins.animal_id = outs.animal_id
WHERE ins.sex_upon_intake LIKE 'Intact%'
    AND (outs.sex_upon_outcome LIKE 'Neutered%' 
         OR outs.sex_upon_outcome LIKE 'Spayed%')
ORDER BY id