# Write your MySQL query statement below
DELETE p1 
From Person p1
Join Person p2
On p1.email =  p2.email AND p1.id > p2.id