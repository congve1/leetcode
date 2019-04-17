# 删除重复的电子邮箱

## 描述

编写一个 SQL 查询，来删除 `Person` 表中所有重复的电子邮箱，重复的邮箱里只保留  **Id  ** _最小  _的那个。

    
    
    +----+------------------+
    | Id | Email            |
    +----+------------------+
    | 1  | john@example.com |
    | 2  | bob@example.com  |
    | 3  | john@example.com |
    +----+------------------+
    Id 是这个表的主键。
    

例如，在运行你的查询语句之后，上面的 `Person` 表应返回以下几行:

    
    
    +----+------------------+
    | Id | Email            |
    +----+------------------+
    | 1  | john@example.com |
    | 2  | bob@example.com  |
    +----+------------------+
    



# Delete Duplicate Emails

## Description



Write a SQL query to **delete** all duplicate email entries in a table named `Person`, keeping only unique emails based on its _smallest_ **Id**.

    
    
    +----+------------------+
    | Id | Email            |
    +----+------------------+
    | 1  | john@example.com |
    | 2  | bob@example.com  |
    | 3  | john@example.com |
    +----+------------------+
    Id is the primary key column for this table.
    

For example, after running your query, the above `Person` table should have the following rows:

    
    
    +----+------------------+
    | Id | Email            |
    +----+------------------+
    | 1  | john@example.com |
    | 2  | bob@example.com  |
    +----+------------------+
    

**Note:**

Your output is the whole `Person` table after executing your sql. Use `delete` statement.


**Tags:** 

**Difficulty:** Easy

**思路:**
