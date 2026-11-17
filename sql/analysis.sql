-- Run after python3 src/build.py
SELECT category, COUNT(*) AS products, ROUND(AVG(price_usd),2) AS avg_price FROM products GROUP BY category ORDER BY products DESC;
SELECT brand_name, COUNT(*) AS products, SUM(review_count_dataset) AS observed_reviews FROM products GROUP BY brand_name HAVING COUNT(*) >= 10 ORDER BY observed_reviews DESC LIMIT 20;
SELECT product_name, brand_name, price_usd, review_count_dataset, review_avg_dataset FROM products WHERE review_count_dataset >= 50 ORDER BY review_avg_dataset DESC LIMIT 25;