# 二叉树的堂兄弟节点

## 描述

在二叉树中，根节点位于深度 `0` 处，每个深度为 `k` 的节点的子节点位于深度 `k+1` 处。

如果二叉树的两个节点深度相同，但 **父节点不同** ，则它们是一对 _堂兄弟节点_ 。

我们给出了具有唯一值的二叉树的根节点 `root`，以及树中两个不同节点的值 `x` 和 `y`。

只有与值 `x` 和 `y` 对应的节点是堂兄弟节点时，才返回 `true`。否则，返回 `false`。



**示例 1：  
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-01.png)**

    
    
    **输入：** root = [1,2,3,4], x = 4, y = 3
    **输出：** false
    

**示例 2：  
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-02.png)**

    
    
    **输入：** root = [1,2,3,null,4,null,5], x = 5, y = 4
    **输出：** true
    

**示例 3：**

**![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-03.png)**

    
    
    **输入：** root = [1,2,3,null,4], x = 2, y = 3
    **输出：** false



**提示：**

  1. 二叉树的节点数介于 `2` 到 `100` 之间。
  2. 每个节点的值都是唯一的、范围为 `1` 到 `100` 的整数。





# Cousins in Binary Tree

## Description



In a binary tree, the root node is at depth `0`, and children of each depth `k` node are at depth `k+1`.

Two nodes of a binary tree are _cousins_ if they have the same depth, but have **different parents**.

We are given the `root` of a binary tree with unique values, and the values `x` and `y` of two different nodes in the tree.

Return `true` if and only if the nodes corresponding to the values `x` and `y` are cousins.



**Example 1:  
![](https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png)**

    
    
    **Input:** root = [1,2,3,4], x = 4, y = 3
    **Output:** false
    

**Example 2:  
![](https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)**

    
    
    **Input:** root = [1,2,3,null,4,null,5], x = 5, y = 4
    **Output:** true
    

**Example 3:**

**![](https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png)**

    
    
    **Input:** root = [1,2,3,null,4], x = 2, y = 3
    **Output:** false



**Note:**

  1. The number of nodes in the tree will be between `2` and `100`.
  2. Each node has a unique integer value from `1` to `100`.




**Tags:** Tree, Breadth-first Search

**Difficulty:** Easy

**思路:**