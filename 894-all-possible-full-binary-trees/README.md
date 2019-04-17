# 所有可能的满二叉树

## 描述

_满二叉树_ 是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 `N` 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个`结点`都 **必须** 有 `node.val=0`。

你可以按任何顺序返回树的最终列表。



**示例：**

    
    
    **输入：** 7
    **输出：** [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    **解释：**
    ![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/fivetrees.png)
    



**提示：**

  * `1 <= N <= 20`



# All Possible Full Binary Trees

## Description



A _full binary tree_  is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with `N` nodes.  Each element of the answer is the root node of one possible tree.

Each `node` of each tree in the answer **must** have `node.val = 0`.

You may return the final list of trees in any order.



**Example 1:**

    
    
    **Input:** 7
    **Output:** [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    **Explanation:**
    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png)
    



**Note:**

  * `1 <= N <= 20`


**Tags:** Tree, Recursion

**Difficulty:** Medium

**思路:**
