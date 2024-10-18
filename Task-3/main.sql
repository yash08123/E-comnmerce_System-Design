-- 1.Top 5 customers by book quantity in the last year:

SELECT c.customer_id, c.name, SUM(od.quantity) AS total_books
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.order_date >= CURDATE() - INTERVAL 1 YEAR
GROUP BY c.customer_id, c.name
ORDER BY total_books DESC
LIMIT 5;


-- 2.Total revenue by each author:
SELECT b.author, SUM(b.price * od.quantity) AS total_revenue
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.author;


-- 3.Books ordered more than 10 times with total quantity:
SELECT b.title, SUM(od.quantity) AS total_quantity
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.title
HAVING total_quantity > 10;

