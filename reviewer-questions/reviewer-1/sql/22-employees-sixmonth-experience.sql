SELECT *
FROM employees
WHERE joining_date <= CURRENT_DATE - INTERVAL '6 months';