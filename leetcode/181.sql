# 181.  Employees Earning More Than Their Managers

# Approach 1. WHERE
SELECT e.Name as Employee 
FROM Employee e, Employee m
WHERE e.ManagerId = m.Id and e.Salary > m.Salary;

# Approach 2. JOIN and WHERE
SELECT e.name AS Employee 
FROM Employee e
JOIN Employee AS m
ON e.ManagerId = m.Id
WHERE e.Salary > m.Salary;