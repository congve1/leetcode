# 二叉树剪枝

## 描述

给定二叉树根结点 `root` ，此外树的每个结点的值要么是 0，要么是 1。

返回移除了所有不包含 1 的子树的原二叉树。

( 节点 X 的子树为 X 本身，以及所有 X 的后代。)

    
    
    **示例1:**
    **输入:** [1,null,0,0,1]
    **输出:** [1,null,0,null,1]
     
    **解释:** 
    只有红色节点满足条件"所有不包含 1 的子树"。
    右图为返回的答案。
    
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)
    
    
    
    **示例2:**
    **输入:** [1,0,1,0,0,0,1]
    **输出:** [1,null,1,null,1]
    
    
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)
    
    
    
    **示例3:**
    **输入:** [1,1,0,1,1,0,1,0]
    **输出:** [1,1,0,1,1,null,1]
    
    
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)
    

**说明:**

  * 给定的二叉树最多有 `100` 个节点。
  * 每个节点的值只会为 `0` 或 `1` 。



# Binary Tree Pruning

## Description



We are given the head node `root` of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

    
    
    **Example 1:**
    **Input:** [1,null,0,0,1]
    **Output:** [1,null,0,null,1]
     
    **Explanation:** 
    Only the red nodes satisfy the property "every subtree not containing a 1".
    The diagram on the right represents the answer.
    
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)
    
    
    
    **Example 2:**
    **Input:** [1,0,1,0,0,0,1]
    **Output:** [1,null,1,null,1]
    
    
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)
    
    
    
    **Example 3:**
    **Input:** [1,1,0,1,1,0,1,0]
    **Output:** [1,1,0,1,1,null,1]
    
    
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)
    

**Note:**

  * The binary tree will have at most `100 nodes`.
  * The value of each node will only be `0` or `1`.


**Tags:** Tree

**Difficulty:** Medium

**思路:**