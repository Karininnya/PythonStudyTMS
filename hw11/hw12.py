CREATE DATABASE homework;
CREATE TABLE employees
(
    id         SERIAL PRIMARY KEY,
    name VARCHAR(50),
    position  VARCHAR,
    department VARCHAR,
    salary FLOAT
);
INSERT INTO employees (name, position, department, salary)
VALUES ('Egor', 'manager', 'sales_departmenr', 3000),
        ('Anna', 'front_end_developer', 'IT_departmenr', 4000),
        ('Sasha', 'chief_accounter', 'account_department', 5000);
UPDATE employees SET salary = 6000 WHERE name = 'Anna';
UPDATE employees SET position = 'senior_front_end_developer' WHERE position = 'front_end_developer';
ALTER TABLE employees ADD COLUMN hire_date DATETIME;

INSERT INTO employees (hire_date) VALUES (CURDATE('2020.03.05')),
        (CURDATE('2020.03.05')),
        (CURDATE('2020.03.05'));
SELECT name, position FROM employees WHERE position LIKE 'manager';
SELECT name, position, salary FROM employees WHERE salary > 5000;
SELECT name, position FROM employees WHERE department LIKE 'account_department';
SELECT AVG(salary) AS avg_salary
FROM employees;
DROP TABLE employees;