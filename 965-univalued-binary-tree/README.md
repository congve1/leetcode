# 单值二叉树

## 描述

如果二叉树每个节点都具有相同的值，那么该二叉树就是 _单值_ 二叉树。

只有给定的树是单值二叉树时，才返回 `true`；否则返回 `false`。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50104-pm.png)

    
    
    **输入：** [1,1,1,1,1,null,1]
    **输出：** true
    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50050-pm.png)

    
    
    **输入：** [2,2,2,5,2]
    **输出：** false
    



**提示：**

  1. 给定树的节点数范围是 `[1, 100]`。
  2. 每个节点的值都是整数，范围为 `[0, 99]` 。



# Univalued Binary Tree

## Description



A binary tree is _univalued_ if every node in the tree has the same value.

Return `true` if and only if the given tree is univalued.



**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png)

    
    
    **Input:** [1,1,1,1,1,null,1]
    **Output:** true
    

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png)

    
    
    **Input:** [2,2,2,5,2]
    **Output:** false
    



**Note:**

  1. The number of nodes in the given tree will be in the range `[1, 100]`.
  2. Each node's value will be an integer in the range `[0, 99]`.


**Tags:** Tree

**Difficulty:** Easy

**思路:**
