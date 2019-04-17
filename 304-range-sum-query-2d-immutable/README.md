# 二维区域和检索 - 矩阵不可变

## 描述

给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 ( _row_ 1,  _col_ 1) ，右下角为 ( _row_ 2,  _col_ 2)。

![Range Sum Query 2D](/static/images/courses/range_sum_query_2d.png)  
上图子矩阵左上角 (row1, col1) = **(2, 1)**  ，右下角(row2, col2) = **(4, 3)，** 该子矩形内元素的总和为 8。

**示例:**

    
    
    给定 matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    
    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12
    

**说明:**

  1. 你可以假设矩阵不可变。
  2. 会多次调用  _sumRegion  _方法 _。_
  3. 你可以假设  _row_ 1 ≤ _row_ 2 且  _col_ 1 ≤ _col_ 2。



# Range Sum Query 2D - Immutable

## Description



Given a 2D matrix _matrix_ , find the sum of the elements inside the rectangle defined by its upper left corner ( _row_ 1, _col_ 1) and lower right corner ( _row_ 2, _col_ 2).

![Range Sum Query 2D](/static/images/courses/range_sum_query_2d.png)  
The above rectangle (with the red border) is defined by (row1, col1) = **(2, 1)** and (row2, col2) = **(4, 3)** , which contains sum = **8**.

**Example:**  

    
    
    Given matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    
    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12
    

**Note:**  

  1. You may assume that the matrix does not change.
  2. There are many calls to _sumRegion_ function.
  3. You may assume that _row_ 1 ≤ _row_ 2 and _col_ 1 ≤ _col_ 2.


**Tags:** Dynamic Programming

**Difficulty:** Medium

**思路:**
