# 回旋镖的数量

## 描述

给定平面上 _  n _对不同的点，"回旋镖" 是由点表示的元组 `(i, j, k)` ，其中 `i` 和 `j` 之间的距离和 `i` 和 `k` 之间的距离相等（ **需要考虑元组的顺序** ）。

找到所有回旋镖的数量。你可以假设 _  n _最大为 **500** ，所有点的坐标在闭区间 **[-10000, 10000]** 中。

**示例:**

    
    
    **输入:**
    [[0,0],[1,0],[2,0]]
    
    **输出:**
    2
    
    **解释:**
    两个回旋镖为 **[[1,0],[0,0],[2,0]]** 和 **[[1,0],[2,0],[0,0]]**
    



# Number of Boomerangs

## Description



Given _n_ points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points `(i, j, k)` such that the distance between `i` and `j` equals the distance between `i` and `k` ( **the order of the tuple matters** ).

Find the number of boomerangs. You may assume that _n_ will be at most **500** and coordinates of points are all in the range **[-10000, 10000]** (inclusive).

**Example:**  

    
    
    **Input:**
    [[0,0],[1,0],[2,0]]
    
    **Output:**
    2
    
    **Explanation:**
    The two boomerangs are **[[1,0],[0,0],[2,0]]** and **[[1,0],[2,0],[0,0]]**
    


**Tags:** Hash Table

**Difficulty:** Easy

**思路:**
