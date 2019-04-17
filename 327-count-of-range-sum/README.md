# 区间和的个数

## 描述

给定一个整数数组 `nums`，返回区间和在 `[lower, upper]` 之间的个数，包含 `lower` 和 `upper`。  
区间和 `S(i, j)` 表示在 `nums` 中，位置从 `i` 到 `j` 的元素之和，包含 `i` 和 `j` (`i` ≤ `j`)。

**说明:**  
最直观的算法复杂度是  _O_ ( _n_ 2) ，请在此基础上优化你的算法。

**示例:**

    
    
    **输入:** _nums_ = [-2,5,-1], _lower_ = -2, _upper_ = 2,
    **输出:** 3 
    **解释:** 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
    



# Count of Range Sum

## Description



Given an integer array `nums`, return the number of range sums that lie in `[lower, upper]` inclusive.  
Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and `j` (`i` ≤ `j`), inclusive.

**Note:**  
A naive algorithm of _O_ ( _n_ 2) is trivial. You MUST do better than that.

**Example:**

    
    
    **Input:** _nums_ = [-2,5,-1], _lower_ = -2, _upper_ = 2,
    **Output:** 3 
    **Explanation:** The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
    


**Tags:** Binary Search Tree, Divide and Conquer

**Difficulty:** Hard

**思路:**
