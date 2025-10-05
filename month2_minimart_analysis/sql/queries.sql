asic Queries

-- All customers
SELECT * FROM customers;

-- Filter products by category
SELECT * FROM products WHERE category='Drinks';

-- Recent orders
SELECT * FROM orders ORDER BY order_date DESC;


Aggregations

-- Total orders
SELECT COUNT(*) AS total_orders FROM orders;

-- Revenue per prod
SELECT p.product_name, SUM(p.price * o.quantity) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;

-- Average product price
SELECT AVG(price) AS avg_price FROM products;


Joins

-- Detailed order details
SELECT o.order_id, c.name AS customer, p.product_name, o.quantity, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;

-- List all customers n orders
SELECT c.name AS customer, o.order_id, p.product_name, o.quantity
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN products p ON o.product_id = p.product_id;

-- Show all products even not ordered
SELECT p.product_name, o.order_id
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id;
