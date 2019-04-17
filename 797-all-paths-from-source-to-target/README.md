# 所有可能的路径

## 描述

给一个有 `n` 个结点的有向无环图，找到所有从 `0` 到 `n-1` 的路径并输出（不要求按顺序）

二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点（译者注：有向图是有方向的，即规定了a->b你就不能从b->a）空就是没有下一个结点了。

    
    
    **示例:**
    **输入:** [[1,2], [3], [3], []] 
    **输出:** [[0,1,3],[0,2,3]] 
    **解释:** 图是这样的:
    0--->1
    |    |
    v    v
    2--->3
    这有两条路: 0 -> 1 -> 3 和 0 -> 2 -> 3.
    

**提示:**

  * 结点的数量会在范围 `[2, 15]` 内。
  * 你可以把路径以任意顺序输出，但在路径内的结点的顺序必须保证。



# All Paths From Source to Target

## Description



Given a directed, acyclic graph of `N` nodes.  Find all possible paths from node `0` to node `N-1`, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

    
    
    **Example:**
    **Input:** [[1,2], [3], [3], []] 
    **Output:** [[0,1,3],[0,2,3]] 
    **Explanation:** The graph looks like this:
    0--->1
    |    |
    v    v
    2--->3
    There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    

**Note:**

  * The number of nodes in the graph will be in the range `[2, 15]`.
  * You can print different paths in any order, but you should keep the order of nodes inside one path.


**Tags:** 

**Difficulty:** Medium

**思路:**
