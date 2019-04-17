# 恢复二叉搜索树

## 描述

二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

**示例  1:**

    
    
    **输入:** [1,3,null,null,2]
    
       1
      /
     3
      \
       2
    
    **输出:** [3,1,null,null,2]
    
       3
      /
     1
      \
       2
    

**示例  2:**

    
    
    **输入:** [3,1,4,null,null,2]
    
      3
     / \
    1   4
       /
      2
    
    **输出:** [2,1,4,null,null,3]
    
      2
     / \
    1   4
       /
      3

**进阶:**

  * 使用 O( _n_ ) 空间复杂度的解法很容易实现。
  * 你能想出一个只使用常数空间的解决方案吗？



# Recover Binary Search Tree

## Description



Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

**Example 1:**

    
    
    **Input:** [1,3,null,null,2]
    
       1
      /
     3
      \
       2
    
    **Output:** [3,1,null,null,2]
    
       3
      /
     1
      \
       2
    

**Example 2:**

    
    
    **Input:** [3,1,4,null,null,2]
    
      3
     / \
    1   4
       /
      2
    
    **Output:** [2,1,4,null,null,3]
    
      2
     / \
    1   4
       /
      3
    

**Follow up:**

  * A solution using O( _n_ ) space is pretty straight forward.
  * Could you devise a constant space solution?


**Tags:** Tree, Depth-first Search

**Difficulty:** Hard

**思路:**
