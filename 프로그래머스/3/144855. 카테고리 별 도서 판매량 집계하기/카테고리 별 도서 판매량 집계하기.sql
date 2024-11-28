-- 코드를 입력하세요
SELECT
    BOOK.CATEGORY,
    SUM(BOOK_SALES.SALES) AS TOTAL_SALES
FROM
    BOOK
    
LEFT JOIN
    BOOK_SALES ON BOOK_SALES.BOOK_ID = BOOK.BOOK_ID
    
WHERE
    DATE_FORMAT(BOOK_SALES.SALES_DATE, '%Y-%m') = '2022-01'
    
GROUP BY
    BOOK.CATEGORY

ORDER BY
    BOOK.CATEGORY ASC