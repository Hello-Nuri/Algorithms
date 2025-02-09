SELECT
    E.ID,
    COALESCE(C.CHILD,0) AS CHILD_COUNT
FROM
    ECOLI_DATA E
LEFT JOIN
    (SELECT
        PARENT_ID AS ID,
        SUM(IF(ID,1,0)) AS CHILD 
    FROM
        ECOLI_DATA
    WHERE
        PARENT_ID IS NOT NULL
    GROUP BY
        PARENT_ID) AS C
ON
    E.ID = C.ID

ORDER BY
    E.ID
