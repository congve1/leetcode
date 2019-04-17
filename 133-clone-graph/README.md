# 克隆图

## 描述

给定无向[ **连通**](https://baike.baidu.com/item/连通图/6460995?fr=aladdin)图中一个节点的引用，返回该图的[ **深拷贝**](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)（克隆）。图中的每个节点都包含它的值 `val`（`Int`） 和其邻居的列表（`list[Node]`）。

**示例：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/113_sample.png)

    
    
    **输入：** {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
    
    **解释：**
    节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
    节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
    节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
    节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
    



**提示：**

  1. 节点数介于 1 到 100 之间。
  2. 无向图是一个[简单图](https://baike.baidu.com/item/简单图/1680528?fr=aladdin)，这意味着图中没有重复的边，也没有自环。
  3. 由于图是无向的，如果节点 _p_ 是节点 _q_ 的邻居，那么节点 _q_ 也必须是节点 _p_  的邻居。
  4. 必须将 **给定节点的拷贝** 作为对克隆图的引用返回。



# Clone Graph

## Description



Given a reference of a node in a  **[connected](https://en.wikipedia.org/wiki/Connectivity_\(graph_theory\)#Connected_graph)**  undirected graph, return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph. Each node in the graph contains a val (`int`) and a list (`List[Node]`) of its neighbors.



**Example:**

![](https://assets.leetcode.com/uploads/2019/02/19/113_sample.png)

    
    
    **Input:** {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
    
    **Explanation:**
    Node 1's value is 1, and it has two neighbors: Node 2 and 4.
    Node 2's value is 2, and it has two neighbors: Node 1 and 3.
    Node 3's value is 3, and it has two neighbors: Node 2 and 4.
    Node 4's value is 4, and it has two neighbors: Node 1 and 3.
    



**Note:**

  1. The number of nodes will be between 1 and 100.
  2. The undirected graph is a [simple graph](https://en.wikipedia.org/wiki/Graph_\(discrete_mathematics\)#Simple_graph), which means no repeated edges and no self-loops in the graph.
  3. Since the graph is undirected, if node _p_  has node _q_  as neighbor, then node _q_  must have node _p_  as neighbor too.
  4. You must return the **copy of the given node** as a reference to the cloned graph.


**Tags:** Depth-first Search, Breadth-first Search, Graph

**Difficulty:** Medium

**思路:**
