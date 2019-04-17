# 强整数

## 描述

给定两个正整数 `x` 和 `y`，如果某一整数等于 `x^i + y^j`，其中整数 `i >= 0` 且 `j >= 0`，那么我们认为该整数是一个 _强整数_ 。

返回值小于或等于 `bound` 的所有 _强整数_ 组成的列表。

你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。



**示例 1：**

    
    
    **输入：** x = 2, y = 3, bound = 10
    **输出：** [2,3,4,5,7,9,10]
    **解释：**
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2
    

**示例  2：**

    
    
    **输入：** x = 3, y = 5, bound = 15
    **输出：** [2,4,6,8,10,14]
    



**提示：**

  * `1 <= x <= 100`
  * `1 <= y <= 100`
  * `0 <= bound <= 10^6`



# Powerful Integers

## Description



Given two positive integers `x` and `y`, an integer is _powerful_  if it is equal to `x^i + y^j` for some integers `i >= 0` and `j >= 0`.

Return a list of all _powerful_ integers that have value less than or equal to `bound`.

You may return the answer in any order.  In your answer, each value should occur at most once.



**Example 1:**

    
    
    **Input:** x = 2, y = 3, bound = 10
    **Output:** [2,3,4,5,7,9,10]
    **Explanation:**
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2
    

**Example 2:**

    
    
    **Input:** x = 3, y = 5, bound = 15
    **Output:** [2,4,6,8,10,14]
    



**Note:**

  * `1 <= x <= 100`
  * `1 <= y <= 100`
  * `0 <= bound <= 10^6`


**Tags:** Hash Table, Math

**Difficulty:** Easy

**思路:**
