# 最大整除子集

## 描述

给出一个由 **无重复的** 正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。



**示例 1:**

    
    
    **输入:** [1,2,3]
    **输出:** [1,2] (当然, [1,3] 也正确)
    

**示例 2:**

    
    
    **输入:** [1,2,4,8]
    **输出:** [1,2,4,8]
    



# Largest Divisible Subset

## Description



Given a set of **distinct** positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

**Example 1:**

    
    
    **Input:** [1,2,3]
    **Output:** [1,2] (of course, [1,3] will also be ok)
    

**Example 2:**

    
    
    **Input:** [1,2,4,8]
    **Output:** [1,2,4,8]
    


**Tags:** Math, Dynamic Programming

**Difficulty:** Medium

**思路:**
