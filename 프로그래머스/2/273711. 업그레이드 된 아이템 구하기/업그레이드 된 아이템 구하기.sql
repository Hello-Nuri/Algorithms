SELECT
    T.ITEM_ID,
    I.ITEM_NAME,
    I.RARITY
FROM
    ITEM_TREE T

JOIN
    ITEM_INFO I
ON
    I.ITEM_ID = T.ITEM_ID

WHERE
     T.PARENT_ITEM_ID IN (SELECT
                            ITEM_ID
                         FROM
                            ITEM_INFO
                            WHERE RARITY LIKE 'RARE')
ORDER BY
    ITEM_ID DESC