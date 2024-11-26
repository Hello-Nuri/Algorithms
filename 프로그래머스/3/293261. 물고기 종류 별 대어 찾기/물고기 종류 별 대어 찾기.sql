-- 각 물고기 종류(FISH_TYPE)별로 LENGTH가 가장 큰 행을 찾기 > 서브쿼리 또는 윈도우함수
SELECT
SUB.ID,
N.FISH_NAME,
SUB.LENGTH
FROM
    FISH_NAME_INFO N
JOIN
    ( 
    SELECT
        F.ID,
        MAXFISH.FISH_TYPE,
        MAXFISH.LENGTH
    FROM
        FISH_INFO F
    JOIN
        ( SELECT
                F.FISH_TYPE,
                MAX(F.LENGTH) AS LENGTH
            FROM
                FISH_INFO F
            WHERE
                F.LENGTH IS NOT NULL
            GROUP BY
                F.FISH_TYPE
        ) MAXFISH 
    ON
        F.FISH_TYPE = MAXFISH.FISH_TYPE
    
    WHERE
        F.LENGTH = MAXFISH.LENGTH
) SUB
ON
    N.FISH_TYPE = SUB.FISH_TYPE