# 182. Duplicate Emails

# Approach 1. Group by, having
SELECT Email
FROM Person 
GROUP BY Email
HAVING 
    COUNT(*) > 1

# Approach 2. Temp table
SELECT Email FROM
(
  SELECT Email, count(Email) AS num
  FROM Person
  GROUP BY Email
) AS statistic
WHERE num > 1