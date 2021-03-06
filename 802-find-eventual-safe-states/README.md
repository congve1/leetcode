# 找到最终的安全状态

## 描述

在有向图中, 我们从某个节点和每个转向处开始, 沿着图的有向边走。 如果我们到达的节点是终点 (即它没有连出的有向边), 我们停止。

现在, 如果我们最后能走到终点，那么我们的起始节点是 _最终安全_ 的。 更具体地说, 存在一个自然数 `K`,  无论选择从哪里开始行走, 我们走了不到 `K` 步后必能停止在一个终点。

哪些节点最终是安全的？ 结果返回一个有序的数组。

该有向图有 `N` 个节点，标签为 `0, 1, ..., N-1`, 其中 `N` 是 `graph` 的节点数.  图以以下的形式给出: `graph[i]` 是节点 `j` 的一个列表，满足 `(i, j)` 是图的一条有向边。

    
    
    **示例：**
    **输入：** graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    **输出：** [2,4,5,6]
    这里是上图的示意图。
    
    

![Illustration of graph](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png)

**提示：**

  * `graph` 节点数不超过 `10000`.
  * 图的边数不会超过 `32000`.
  * 每个 `graph[i]` 被排序为不同的整数列表， 在区间 `[0, graph.length - 1]` 中选取。



# Find Eventual Safe States

## Description



In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is _eventually safe  _if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number `K` so that for any choice of where to walk, we must have stopped at a terminal node in less than `K` steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has `N` nodes with labels `0, 1, ..., N-1`, where `N` is the length of `graph`.  The graph is given in the following form: `graph[i]` is a list of labels `j` such that `(i, j)` is a directed edge of the graph.

    
    
    **Example:**
    **Input:** graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    **Output:** [2,4,5,6]
    Here is a diagram of the above graph.
    
    

![Illustration of graph](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png)

**Note:**

  * `graph` will have length at most `10000`.
  * The number of edges in the graph will not exceed `32000`.
  * Each `graph[i]` will be a sorted list of different integers, chosen within the range `[0, graph.length - 1]`.


**Tags:** Depth-first Search, Graph

**Difficulty:** Medium

**思路:**
