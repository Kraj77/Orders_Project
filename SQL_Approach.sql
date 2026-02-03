-- SQL Approach for the problem

SELECT
	c.customer_id,
	age,
	item_name,
	CAST(SUM(COALESCE(quantity, 0)) AS INTEGER) AS quantity
FROM
	Customer c
INNER JOIN Sales s
	ON c.customer_id = s.customer_id
INNER JOIN 
	Orders o
ON s.sales_id = o.sales_id
INNER JOIN
	Items  i
ON o.item_id = i.item_id
	WHERE age BETWEEN 18 AND 36
GROUP BY c.customer_id,age,item_name
	HAVING SUM(COALESCE(quantity, 0)) > 0
ORDER BY c.customer_id,item_name;
