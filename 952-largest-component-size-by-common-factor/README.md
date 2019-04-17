# 按公因数计算最大组件大小

## 描述

给定一个由不同正整数的组成的非空数组 `A`，考虑下面的图：

  * 有 `A.length` 个节点，按从 `A[0]` 到 `A[A.length - 1]` 标记；
  * 只有当 `A[i]` 和 `A[j]` 共用一个大于 1 的公因数时，`A[i]` 和 `A[j]` 之间才有一条边。

返回图中最大连通组件的大小。



**示例 1：**

    
    
    **输入：** [4,6,15,35]
    **输出：** 4
    ![](https://assets.leetcode-cn.com/aliyun-lc-uploads/uploads/2018/12/01/ex1.png)![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/01/ex1.png)
    

**示例 2：**

    
    
    **输入：** [20,50,9,63]
    **输出：** 2
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/01/ex2.png)
    

**示例 3：**

    
    
    **输入：** [2,3,6,7,4,12,21,39]
    **输出：** 8
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/01/ex3.png)
    



**提示：**

  1. `1 <= A.length <= 20000`
  2. `1 <= A[i] <= 100000`



# Largest Component Size by Common Factor

## Description



Given a non-empty array of unique positive integers `A`, consider the following graph:

  * There are `A.length` nodes, labelled `A[0]` to `A[A.length - 1];`
  * There is an edge between `A[i]` and `A[j]` if and only if `A[i]` and `A[j]` share a common factor greater than 1.

Return the size of the largest connected component in the graph.



**Example 1:**

    
    
    **Input:** [4,6,15,35]
    **Output:** 4
    ![](https://assets.leetcode.com/uploads/2018/12/01/ex1.png)
    

**Example 2:**

    
    
    **Input:** [20,50,9,63]
    **Output:** 2
    ![](https://assets.leetcode.com/uploads/2018/12/01/ex2.png)
    

**Example 3:**

    
    
    **Input:** [2,3,6,7,4,12,21,39]
    **Output:** 8
    ![](https://assets.leetcode.com/uploads/2018/12/01/ex3.png)
    

**Note:**

  1. `1 <= A.length <= 20000`
  2. `1 <= A[i] <= 100000`


**Tags:** Union Find, Math

**Difficulty:** Hard

**思路:**
