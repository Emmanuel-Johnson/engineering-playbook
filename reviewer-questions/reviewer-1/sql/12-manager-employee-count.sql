SELECT m.employee_name AS manager_name,
       COUNT(e.employee_id) AS total_employees
FROM Employees AS e
INNER JOIN Employees AS m
ON e.manager_id = m.employee_id
GROUP BY m.employee_name;