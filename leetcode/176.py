# 176. Second Highest Salary

# Approach 1.
SELECT
    (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

# Approach 2. using IFNULL
SELECT
    IFNULL(
      (
        SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1
       ),
    NULL) AS SecondHighestSalary;
