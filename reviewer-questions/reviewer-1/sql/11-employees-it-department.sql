SELECT e.employee_name, d.department_name
FROM Employees AS e
INNER JOIN Departments AS d
ON e.department_id = d.department_id
WHERE d.department_name = 'IT';