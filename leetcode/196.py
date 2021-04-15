# 196. Delete Duplicate Emails
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

DELETE FROM Person WHERE Id NOT IN 
(SELECT * FROM(
    SELECT MIN(Id) FROM Person GROUP BY Email) as p)


WITH t AS (
    SELECT Id, Email, RANK() OVER(Partition By Email Order by Id) as rnk from Person)

DELETE FROM Person WHERE Id IN (SELECT Id from t where rnk > 1);
