# -- Add animal_outs content in other table which is fulled as 0~23 hour and 0 values
WITH RECURSIVE hour_creator AS(
    SELECT 
        0 AS HOUR
    UNION ALL
    SELECT
        HOUR + 1
    FROM
        HOUR_creator
    WHERE
        HOUR < 23
)
SELECT 
hour_creator.HOUR,
COALESCE(C.COUNT,0) AS COUNT 

FROM hour_creator

LEFT JOIN
 ( SELECT
    HOUR(DATETIME) AS hOUR,
    COUNT(ANIMAL_ID) AS COUNT
  FROM
    ANIMAL_OUTS
  WHERE
    HOUR(DATETIME) BETWEEN 0 AND 23
  GROUP BY
    HOUR
  ORDER BY
    HOUR ) C
ON
    hour_creator.HOUR = C.hOUR