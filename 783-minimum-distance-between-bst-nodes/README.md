# 二叉搜索树结点最小距离

## 描述

给定一个二叉搜索树的根结点 `root`, 返回树中任意两节点的差的最小值。

**示例：**

    
    
    **输入:** root = [4,2,6,1,3,null,null]
    **输出:** 1
    **解释:**
    注意，root是树结点对象(TreeNode object)，而不是数组。
    
    给定的树 [4,2,6,1,3,null,null] 可表示为下图:
    
              4
            /   \
          2      6
         / \    
        1   3  
    
    最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。

**注意：**

  1. 二叉树的大小范围在 `2` 到 `100`。
  2. 二叉树总是有效的，每个节点的值都是整数，且不重复。



# Minimum Distance Between BST Nodes

## Description



Given a Binary Search Tree (BST) with the root node `root`, return the minimum difference between the values of any two different nodes in the tree.

**Example :**

    
    
    **Input:** root = [4,2,6,1,3,null,null]
    **Output:** 1
    **Explanation:**
    Note that root is a TreeNode object, not an array.
    
    The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
    
              4
            /   \
          2      6
         / \    
        1   3  
    
    while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
    

**Note:**

  1. The size of the BST will be between 2 and `100`.
  2. The BST is always valid, each node's value is an integer, and each node's value is different.


**Tags:** Binary Search Tree

**Difficulty:** Easy

**思路:**
