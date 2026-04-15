-- Total sales by day
SELECT DATE(date) AS sales_date, SUM(total_amount) AS daily_sales
FROM sales
GROUP BY DATE(date)
ORDER BY sales_date;

-- Top 10 products by revenue
SELECT product_name, SUM(total_amount) AS revenue
FROM sales
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

-- Store performance
SELECT store_id, COUNT(*) AS total_transactions, SUM(total_amount) AS total_revenue
FROM sales
GROUP BY store_id
ORDER BY total_revenue DESC;

-- Inventory levels
SELECT product_id, product_name, SUM(quantity_sold) AS total_sold, AVG(inventory_level) AS avg_inventory
FROM sales
GROUP BY product_id, product_name
ORDER BY avg_inventory ASC;

-- Peak sales hours
SELECT EXTRACT(HOUR FROM date) AS hour, SUM(total_amount) AS revenue
FROM sales
GROUP BY hour
ORDER BY revenue DESC;
