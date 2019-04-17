# 出界的路径数

## 描述

给定一个 **m × n **的网格和一个球。球的起始坐标为  **(i,j)**  ，你可以将球移到 **相邻** 的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你 **最多** 可以移动  **N  **次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 \+ 7 的值。



**示例 1：**

    
    
    **输入:** m = 2, n = 2, N = 2, i = 0, j = 0
    **输出:** 6
    **解释:**
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/out_of_boundary_paths_1.png)
    

**示例 2：**

    
    
    **输入:** m = 1, n = 3, N = 3, i = 0, j = 1
    **输出:** 12
    **解释:**
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/out_of_boundary_paths_2.png)
    



**说明:**

  1. 球一旦出界，就不能再被移动回网格内。
  2. 网格的长度和高度在 [1,50] 的范围内。
  3. N 在 [0,50] 的范围内。



# Out of Boundary Paths

## Description



There is an **m** by **n** grid with a ball. Given the start coordinate **(i,j)** of the ball, you can move the ball to **adjacent** cell or cross the grid boundary in four directions (up, down, left, right). However, you can **at most** move **N** times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 \+ 7.



**Example 1:**

    
    
    **Input:** m = 2, n = 2, N = 2, i = 0, j = 0
    **Output:** 6
    **Explanation:**
    ![](https://assets.leetcode.com/uploads/2018/10/13/out_of_boundary_paths_1.png)
    

**Example 2:**

    
    
    **Input:** m = 1, n = 3, N = 3, i = 0, j = 1
    **Output:** 12
    **Explanation:**
    ![](https://assets.leetcode.com/uploads/2018/10/12/out_of_boundary_paths_2.png)
    



**Note:**

  1. Once you move the ball out of boundary, you cannot move it back.
  2. The length and height of the grid is in range [1,50].
  3. N is in range [0,50].


**Tags:** Depth-first Search, Dynamic Programming

**Difficulty:** Medium

**思路:**
