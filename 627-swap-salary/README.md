# 交换工资

## 描述

给定一个 `salary` 表，如下所示，有 m=男性 和 f=女性 的值 。交换所有的 f 和 m 值（例如，将所有 f 值更改为 m，反之亦然）。要求使用一个更新（Update）语句，并且没有中间临时表。

请注意，你必须编写一个 Update 语句，不要编写任何 Select 语句。



例如:

    
    
    | id | name | sex | salary |
    |----|------|-----|--------|
    | 1  | A    | m   | 2500   |
    | 2  | B    | f   | 1500   |
    | 3  | C    | m   | 5500   |
    | 4  | D    | f   | 500    |
    

运行你所编写的更新语句之后，将会得到以下表:

    
    
    | id | name | sex | salary |
    |----|------|-----|--------|
    | 1  | A    | f   | 2500   |
    | 2  | B    | m   | 1500   |
    | 3  | C    | f   | 5500   |
    | 4  | D    | m   | 500    |
    



# Swap Salary

## Description



Given a table `salary`, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a **single update statement** and no intermediate temp table.

Note that you must write a single update statement, **DO NOT** write any select statement for this problem.



**Example:**

    
    
    | id | name | sex | salary |
    |----|------|-----|--------|
    | 1  | A    | m   | 2500   |
    | 2  | B    | f   | 1500   |
    | 3  | C    | m   | 5500   |
    | 4  | D    | f   | 500    |
    

After running your **update** statement, the above salary table should have the following rows:

    
    
    | id | name | sex | salary |
    |----|------|-----|--------|
    | 1  | A    | f   | 2500   |
    | 2  | B    | m   | 1500   |
    | 3  | C    | f   | 5500   |
    | 4  | D    | m   | 500    |
    


**Tags:** 

**Difficulty:** Easy

**思路:**
