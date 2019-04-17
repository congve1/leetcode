# 体育馆的人流量

## 描述

X 市建了一个新的体育馆，每日人流量信息被记录在这三列信息中： **序号** (id)、 **日期** (date)、  **人流量** (people)。

请编写一个查询语句，找出高峰期时段，要求连续三天及以上，并且每天人流量均不少于100。

例如，表 `stadium`：

    
    
    +------+------------+-----------+
    | id   | date       | people    |
    +------+------------+-----------+
    | 1    | 2017-01-01 | 10        |
    | 2    | 2017-01-02 | 109       |
    | 3    | 2017-01-03 | 150       |
    | 4    | 2017-01-04 | 99        |
    | 5    | 2017-01-05 | 145       |
    | 6    | 2017-01-06 | 1455      |
    | 7    | 2017-01-07 | 199       |
    | 8    | 2017-01-08 | 188       |
    +------+------------+-----------+
    

对于上面的示例数据，输出为：

    
    
    +------+------------+-----------+
    | id   | date       | people    |
    +------+------------+-----------+
    | 5    | 2017-01-05 | 145       |
    | 6    | 2017-01-06 | 1455      |
    | 7    | 2017-01-07 | 199       |
    | 8    | 2017-01-08 | 188       |
    +------+------------+-----------+
    

**Note:**  
每天只有一行记录，日期随着 id 的增加而增加。



# Human Traffic of Stadium

## Description



X city built a new stadium, each day many people visit it and the stats are saved as these columns: **id** , **visit_** **date** , **people**

Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).

For example, the table `stadium`:

    
    
    +------+------------+-----------+
    | id   | visit_date | people    |
    +------+------------+-----------+
    | 1    | 2017-01-01 | 10        |
    | 2    | 2017-01-02 | 109       |
    | 3    | 2017-01-03 | 150       |
    | 4    | 2017-01-04 | 99        |
    | 5    | 2017-01-05 | 145       |
    | 6    | 2017-01-06 | 1455      |
    | 7    | 2017-01-07 | 199       |
    | 8    | 2017-01-08 | 188       |
    +------+------------+-----------+
    

For the sample data above, the output is:

    
    
    +------+------------+-----------+
    | id   | visit_date | people    |
    +------+------------+-----------+
    | 5    | 2017-01-05 | 145       |
    | 6    | 2017-01-06 | 1455      |
    | 7    | 2017-01-07 | 199       |
    | 8    | 2017-01-08 | 188       |
    +------+------------+-----------+
    

**Note:**  
Each day only have one row record, and the dates are increasing with id increasing.


**Tags:** 

**Difficulty:** Hard

**思路:**