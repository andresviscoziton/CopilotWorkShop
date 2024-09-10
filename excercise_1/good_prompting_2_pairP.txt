-- As a human Driver, I am writing an SQL query to get the list of employees who earn more than 50,000 per year.
-- I need to ensure that the query is efficient and takes into account indexes and best practices.

-- Copilot as "Navigator", provides recommendations to improve the efficiency of the query:
-- 1. Select only the necessary columns instead of using '*'.
-- 2. Ensure that there is an index on the 'annual_salary' column to improve performance.
-- 3. Use aliases to improve the readability of the query.

-- Here is the improved SQL query:
    SELECT employee_id, first_name, last_name, annual_salary
    FROM employees
    WHERE annual_salary > 50000;
-- This query selects only the necessary columns and filters the employees based on the annual salary condition.
-- It is efficient and takes into account best practices for SQL queries.


