# Write your MySQL query statement below
select a.name as 'Employee' from Employee a inner join Employee b on a.managerID=b.id where a.salary>b.salary;