# Write your MySQL query statement below
Select name as Customers
From Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
Group by c.id
Having Count(o.customerId) = 0;