# 矩形区域不超过 K 的最大数值和

## 描述

给定一个非空二维矩阵  _matrix  _和一个整数 _k_ ，找到这个矩阵内部不大于 _k_ 的最大矩形和。

**示例:**

    
    
    **输入:** matrix = [[1,0,1],[0,-2,3]], k = 2
    **输出:** 2 
    **解释:**  矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
    

**说明：**

  1. 矩阵内的矩形区域面积必须大于 0。
  2. 如果行数远大于列数，你将如何解答呢？



# Max Sum of Rectangle No Larger Than K

## Description



Given a non-empty 2D matrix _matrix_ and an integer _k_ , find the max sum of a rectangle in the _matrix_ such that its sum is no larger than _k_.

**Example:**

    
    
    **Input:** matrix = [[1,0,1],[0,-2,3]], k = 2
    **Output:** 2 
    **Explanation:**  Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
                 and 2 is the max number no larger than k (k = 2).

**Note:**

  1. The rectangle inside the matrix must have an area > 0.
  2. What if the number of rows is much larger than the number of columns?


**Tags:** Queue, Binary Search, Dynamic Programming

**Difficulty:** Hard

**思路:**
