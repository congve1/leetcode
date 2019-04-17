# 移除最多的同行或同列石头

## 描述

在二维平面上，我们将石头放置在一些整数坐标点上。每个坐标点上最多只能有一块石头。  
  
现在， _move_ 操作将会移除与网格上的某一块石头共享一列或一行的一块石头。  
  
我们最多能执行多少次 _move_ 操作？



**示例 1：**

    
    
    **输入：** stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    **输出：** 5
    

**示例 2：**

    
    
    **输入：** stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    **输出：** 3
    

**示例 3：**

    
    
    **输入：** stones = [[0,0]]
    **输出：** 0
    



**提示：**

  1. `1 <= stones.length <= 1000`
  2. `0 <= stones[i][j] < 10000`



# Most Stones Removed with Same Row or Column

## Description



On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a _move_ consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?



**Example 1:**

    
    
    **Input:** stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    **Output:** 5
    

**Example 2:**

    
    
    **Input:** stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    **Output:** 3
    

**Example 3:**

    
    
    **Input:** stones = [[0,0]]
    **Output:** 0
    



**Note:**

  1. `1 <= stones.length <= 1000`
  2. `0 <= stones[i][j] < 10000`


**Tags:** Depth-first Search, Union Find

**Difficulty:** Medium

**思路:**
