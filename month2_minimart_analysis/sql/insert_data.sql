-- Customers
INSERT INTO customers (name, email, join_date) VALUES
('Alice Kimani', 'alicehome@gmail.com', '2025-01-10'),
('Bob Johnson', 'bobj@gmail.com', '2025-02-05'),
('Charlie Abu', 'charlie@yahoo.com', '2025-03-12'),
('Diana Atieno', 'diana@yahoo.com', '2025-04-22'),
('Ethan Hunt', 'ethan@gmail.com', '2025-05-30');

-- Products
INSERT INTO products (product_name, category, price) VALUES
('Orange Juice', 'Drinks', 3.50),
('Milk', 'Dairy', 2.00),
('Bread', 'Bakery', 1.50),
('Apple', 'Fruits', 0.80),
('Cheese', 'Dairy', 4.00);

-- Orders
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2025-09-01'),
(2, 3, 5, '2025-09-02'),
(3, 2, 1, '2025-09-03'),
(1, 4, 10, '2025-09-04'),
(5, 5, 3, '2025-09-05');
