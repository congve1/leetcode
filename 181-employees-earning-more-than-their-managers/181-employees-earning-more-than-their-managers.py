# Write your MySQL query statement below
Select e.Name as Employee
from Employee e
left join Employee e2
on e.ManagerId = e2.Id
where e.Salary > e2.salary
