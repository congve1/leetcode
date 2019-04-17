# 先序遍历构造二叉树

## 描述

返回与给定先序遍历 `preorder` 相匹配的二叉搜索树（binary **search** tree）的根结点。

_(回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于  `node.left` 的任何后代，值总 `<` `node.val`，而 `node.right` 的任何后代，值总 `>` `node.val`。此外，先序遍历首先显示节点的值，然后遍历 `node.left`，接着遍历 `node.right`。）_



**示例：**

    
    
    **输入：** [8,5,1,7,10,12]
    **输出：** [8,5,10,1,7,null,12]
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/03/08/1266.png)
    



**提示：**

  1. `1 <= preorder.length <= 100`
  2. 先序 `preorder` 中的值是不同的。



# Construct Binary Search Tree from Preorder Traversal

## Description



Return the root node of a binary **search** tree that matches the given `preorder` traversal.

_(Recall that a binary search tree  is a binary tree where for every node, any descendant of `node.left` has a value `<` `node.val`, and any descendant of `node.right` has a value `>` `node.val`.  Also recall that a preorder traversal displays the value of the `node` first, then traverses `node.left`, then traverses `node.right`.)_



**Example 1:**

    
    
    **Input:** [8,5,1,7,10,12]
    **Output:** [8,5,10,1,7,null,12]
    ![](https://assets.leetcode.com/uploads/2019/03/06/1266.png)
    



**Note:**  

  1. `1 <= preorder.length <= 100`
  2. The values of `preorder` are distinct.


**Tags:** Tree

**Difficulty:** Medium

**思路:**
