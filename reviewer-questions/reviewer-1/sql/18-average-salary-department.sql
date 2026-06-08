SELECT d.department_name, AVG(e.salary) AS average_salary
FROM Departments AS d
INNER JOIN Employees AS e
ON d.department_id = e.department_id
GROUP BY d.department_name;