# 最大人工岛

## 描述

在二维地图上， `0`代表海洋， `1`代表陆地，我们最多只能将一格 `0` 海洋变成 `1`变成陆地。

进行填海之后，地图上最大的岛屿面积是多少？（上、下、左、右四个方向相连的 `1` 可形成岛屿）

**示例 1:**

    
    
    **输入:** [[1, 0], [0, 1]]
    **输出:** 3
    **解释:** 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
    

**示例 2:**

    
    
    **输入:** [[1, 1], [1, 0]]
    **输出:** 4
    **解释:** 将一格0变成1，岛屿的面积扩大为 4。

**示例 3:**

    
    
    **输入:** [[1, 1], [1, 1]]
    **输出:** 4
    **解释:** 没有0可以让我们变成1，面积依然为 4。

**说明:**

  * `1 <= grid.length = grid[0].length <= 50`
  * `0 <= grid[i][j] <= 1`



# Making A Large Island

## Description



In a 2D grid of `0`s and `1`s, we change at most one `0` to a `1`.

After, what is the size of the largest island? (An island is a 4-directionally connected group of `1`s).

**Example 1:**

    
    
    **Input:** [[1, 0], [0, 1]]
    **Output:** 3
    **Explanation:** Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
    

**Example 2:**

    
    
    **Input:** [[1, 1], [1, 0]]
    **Output:** 4
    **Explanation:** Change the 0 to 1 and make the island bigger, only one island with area = 4.

**Example 3:**

    
    
    **Input:** [[1, 1], [1, 1]]
    **Output:** 4
    **Explanation:** Can't change any 0 to 1, only one island with area = 4.



Notes:

  * `1 <= grid.length = grid[0].length <= 50`.
  * `0 <= grid[i][j] <= 1`.




**Tags:** Depth-first Search

**Difficulty:** Hard

**思路:**
