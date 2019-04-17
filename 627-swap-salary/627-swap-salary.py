# Write your MySQL query statement below
Update salary
SET
    sex = CASE sex
        When 'm' Then 'f'
        else 'm'
    end;
