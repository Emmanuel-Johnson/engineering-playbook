UPDATE Salaries
SET SalaryAmount = SalaryAmount * 1.10
WHERE EmployeeID IN (
    SELECT e.EmployeeID
    FROM Employees e
    JOIN Departments d
        ON e.DepartmentID = d.DepartmentID
    WHERE d.DepartmentName = 'HR'
);