# 二叉树的完全性检验

## 描述

给定一个二叉树，确定它是否是一个 _完全二叉树_ 。

**[百度百科](https://baike.baidu.com/item/完全二叉树/7773232?fr=aladdin)中对完全二叉树的定义如下：**

若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/complete-binary-tree-1.png)

    
    
    **输入：** [1,2,3,4,5,6]
    **输出：** true
    **解释：** 最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
    

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/complete-binary-tree-2.png)**

    
    
    **输入：** [1,2,3,4,5,null,7]
    **输出：** false
    **解释：** 值为 7 的结点没有尽可能靠向左侧。
    



**提示：**

  1. 树中将会有 1 到 100 个结点。



# Check Completeness of a Binary Tree

## Description



Given a binary tree, determine if it is a _complete binary tree_.

_**Definition of a complete binary tree from[Wikipedia](http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees):**_  
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



**Example 1:**

**![](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png)**

    
    
    **Input:** [1,2,3,4,5,6]
    **Output:** true
    **Explanation:** Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
    

**Example 2:**

**![](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png)**

    
    
    **Input:** [1,2,3,4,5,null,7]
    **Output:** false
    **Explanation:** The node with value 7 isn't as far left as possible.
    



**Note:**

  1. The tree will have between 1 and 100 nodes.


**Tags:** Tree

**Difficulty:** Medium

**思路:**
