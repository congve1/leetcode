# 矩阵中的幻方

## 描述

3 x 3 的幻方是一个填充有 **从 1 到 9** 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。

给定一个由整数组成的 `grid`，其中有多少个 3 × 3 的 "幻方" 子矩阵？（每个子矩阵都是连续的）。



**示例：**

    
    
    **输入:** [[4,3,8,4],
          [9,5,1,9],
          [2,7,6,2]]
    **输出:** 1
    **解释:**
    下面的子矩阵是一个 3 x 3 的幻方：
    438
    951
    276
    
    而这一个不是：
    384
    519
    762
    
    总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
    

**提示:**

  1. `1 <= grid.length <= 10`
  2. `1 <= grid[0].length <= 10`
  3. `0 <= grid[i][j] <= 15`



# Magic Squares In Grid

## Description



A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers **from 1 to 9** such that each row, column, and both diagonals all have the same sum.

Given an `grid` of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



**Example 1:**

    
    
    **Input:** [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    **Output:** 1
    **Explanation:**
    The following subgrid is a 3 x 3 magic square:
    438
    951
    276
    
    while this one is not:
    384
    519
    762
    
    In total, there is only one magic square inside the given grid.
    

**Note:**

  1. `1 <= grid.length <= 10`
  2. `1 <= grid[0].length <= 10`
  3. `0 <= grid[i][j] <= 15`


**Tags:** Array

**Difficulty:** Easy

**思路:**
