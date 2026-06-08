CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);


CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10,2),
    department_id INT,
    
    FOREIGN KEY (department_id)
    REFERENCES Departments(department_id)
);