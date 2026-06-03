SELECT 
    d.DepartmentID,
    d.DepartmentName,
    e.EmployeeID,
    e.FName,
    e.LName,
    e.HireDate
FROM Employees e
JOIN Departments d
    ON e.DepartmentID = d.DepartmentID
WHERE e.HireDate = (
    SELECT MAX(HireDate)
    FROM Employees
    WHERE DepartmentID = e.DepartmentID
);