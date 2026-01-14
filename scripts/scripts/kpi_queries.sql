-- KPI Analysis Queries
-- Author: A Veena

SELECT 
    SUM(sales) AS total_sales,
    SUM(revenue) AS total_revenue,
    AVG(customers) AS avg_customers
FROM business_data;

SELECT 
    month,
    revenue
FROM business_data
ORDER BY revenue DESC;
