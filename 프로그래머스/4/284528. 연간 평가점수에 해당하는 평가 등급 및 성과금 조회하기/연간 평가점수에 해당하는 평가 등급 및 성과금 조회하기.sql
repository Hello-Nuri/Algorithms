-- 코드를 작성해주세요

SELECT
    Subquery.EMP_NO,
    HR_EMPLOYEES.EMP_NAME,
    Subquery.GRADE,
    CASE
        WHEN GRADE LIKE 'S' THEN (SAL / 100 * 20) 
        WHEN GRADE LIKE 'A' THEN (SAL / 100 * 15)
        WHEN GRADE LIKE 'B' THEN (SAL / 100 * 10)
        ELSE (SAL/100 * 0) END AS BONUS
FROM ( 
    SELECT
    EMP_NO,
    CASE
        WHEN AVG(SCORE) >= 96 THEN 'S'
        WHEN AVG(SCORE) >= 90 THEN 'A'
        WHEN AVG(SCORE) >= 80 THEN 'B'
        ELSE 'C' END AS GRADE
 FROM
    HR_GRADE 
 GROUP BY
    EMP_NO
    )  AS Subquery

JOIN
    HR_EMPLOYEES
ON
    Subquery.EMP_NO = HR_EMPLOYEES.EMP_NO

ORDER BY
    EMP_NO