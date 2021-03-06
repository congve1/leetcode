# 翻转等价二叉树

## 描述

我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。

只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X _翻转等价_ 于二叉树 Y。

编写一个判断两个二叉树是否是 _翻转等价_ 的函数。这些树由根节点 `root1` 和 `root2` 给出。



**示例：**

    
    
    **输入：** root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    **输出：** true
    **解释：** We flipped at nodes with values 1, 3, and 5.
    ![Flipped Trees Diagram](https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png)
    



**提示：**

  1. 每棵树最多有 `100` 个节点。
  2. 每棵树中的每个值都是唯一的、在 `[0, 99]` 范围内的整数。





# Flip Equivalent Binary Trees

## Description



For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is _flip equivalent_ to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are _flip equivalent_.  The trees are given by root nodes `root1` and `root2`.



**Example 1:**

    
    
    **Input:** root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    **Output:** true
    **Explanation:** We flipped at nodes with values 1, 3, and 5.
    ![Flipped Trees Diagram](https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png)
    



**Note:**

  1. Each tree will have at most `100` nodes.
  2. Each value in each tree will be a unique integer in the range `[0, 99]`.




**Tags:** Tree

**Difficulty:** Medium

**思路:**
