# 岛屿的周长

## 描述

给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有"湖"（"湖" 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。



**示例 :**

    
    
    **输入:**
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
    
    **输出:** 16
    
    **解释:** 它的周长是下面图片中的 16 个黄色的边：
    
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/island.png)
    



# Island Perimeter

## Description



You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



**Example:**

    
    
    **Input:**
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
    
    **Output:** 16
    
    **Explanation:** The perimeter is the 16 yellow stripes in the image below:
    
    ![](https://assets.leetcode.com/uploads/2018/10/12/island.png)
    


**Tags:** Hash Table

**Difficulty:** Easy

**思路:**
