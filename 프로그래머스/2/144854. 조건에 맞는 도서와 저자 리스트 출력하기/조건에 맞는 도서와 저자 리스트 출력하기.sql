-- 코드를 입력하세요
SELECT
    BOOK.book_id,
    AUTHOR.author_name,
    DATE_FORMAT(BOOK.published_date,'%Y-%m-%d') AS published_date
FROM
    BOOK

JOIN
    AUTHOR
ON
    BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID

WHERE
    category LIKE '경제'

ORDER BY
    published_date