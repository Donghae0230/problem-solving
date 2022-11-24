-- 문제: 입력값 만큼 *로 삼각형 만들기
-- 풀이방식: SQL을 함수처럼 사용하기 위해 저장 프로시저 사용

DELIMITER $$
CREATE PROCEDURE RepeatStars(IN counter INT)
BEGIN
    REPEAT
        SELECT REPEAT('* ', counter);
        SET counter = counter - 1;
    UNTIL counter = 0
    END REPEAT;
END$$
DELIMITER ;
CALL RepeatStars(20);

-- 1) DELIMITER 변경
-- 2) INT 타입의 counter 변수를 입력값으로 받기
-- 3) REPEAT() 함수 사용해서 '*' 출력
-- 4) counter 변수 - 1
-- 5) UNTIL [expression]을 통해 expressio이 true일 때까지 반복 (세미콜론 XXX)
-- 6) END$$로 종료
-- 7) DELIMITER 변경

-- DELIMITER 값을 바꿔주는 이유
-- : 저장 프로시저 작성 완료 전에 SQL문이 실행되는 것을 막기 위해 사용 (; > $$ > ;)
