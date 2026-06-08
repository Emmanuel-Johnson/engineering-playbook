UPDATE Employees
SET salary = salary * 1.10
WHERE department_id IN (
    SELECT department_id
    FROM Departments
    WHERE department_name = 'HR'
);