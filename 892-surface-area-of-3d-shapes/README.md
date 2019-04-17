# 三维形体的表面积

## 描述

在 `N * N` 的网格上，我们放置一些 `1 * 1 * 1 ` 的立方体。

每个值 `v = grid[i][j]` 表示 `v` 个正方体叠放在单元格 `(i, j)` 上。

返回结果形体的总表面积。



**示例 1：**

    
    
    **输入：** [[2]]
    **输出：** 10
    

**示例 2：**

    
    
    **输入：** [[1,2],[3,4]]
    **输出：** 34
    

**示例 3：**

    
    
    **输入：** [[1,0],[0,2]]
    **输出：** 16
    

**示例 4：**

    
    
    **输入：** [[1,1,1],[1,0,1],[1,1,1]]
    **输出：** 32
    

**示例  5：**

    
    
    **输入：** [[2,2,2],[2,1,2],[2,2,2]]
    **输出：** 46
    



**提示：**

  * `1 <= N <= 50`
  * `0 <= grid[i][j] <= 50`



# Surface Area of 3D Shapes

## Description



On a `N * N` grid, we place some `1 * 1 * 1 `cubes.

Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of grid cell `(i, j)`.

Return the total surface area of the resulting shapes.



**Example 1:**

    
    
    **Input:** [[2]]
    **Output:** 10
    

**Example 2:**

    
    
    **Input:** [[1,2],[3,4]]
    **Output:** 34
    

**Example 3:**

    
    
    **Input:** [[1,0],[0,2]]
    **Output:** 16
    

**Example 4:**

    
    
    **Input:** [[1,1,1],[1,0,1],[1,1,1]]
    **Output:** 32
    

**Example 5:**

    
    
    **Input:** [[2,2,2],[2,1,2],[2,2,2]]
    **Output:** 46
    



**Note:**

  * `1 <= N <= 50`
  * `0 <= grid[i][j] <= 50`


**Tags:** Geometry, Math

**Difficulty:** Easy

**思路:**
