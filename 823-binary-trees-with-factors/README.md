# 带因子的二叉树

## 描述

给出一个含有不重复整数元素的数组，每个整数均大于 1。

我们用这些整数来构建二叉树，每个整数可以使用任意次数。

其中：每个非叶结点的值应等于它的两个子结点的值的乘积。

满足条件的二叉树一共有多少个？返回的结果应 **模除 10 ** 9 + 7** 。



**示例 1:**

    
    
    **输入:** A = [2, 4]
    **输出:** 3
    **解释:** 我们可以得到这些二叉树: [2], [4], [4, 2, 2]

**示例 2:**

    
    
    **输入:** A = [2, 4, 5, 10]
    **输出:** 7
    **解释:** 我们可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].



**提示:**

  1. `1 <= A.length <= 1000.`
  2. `2 <= A[i] <= 10 ^ 9`.



# Binary Trees With Factors

## Description



Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer **modulo 10 ** 9 + 7**.

**Example 1:**

    
    
    **Input:** A = [2, 4]
    **Output:** 3
    **Explanation:** We can make these trees: [2], [4], [4, 2, 2]

**Example 2:**

    
    
    **Input:** A = [2, 4, 5, 10]
    **Output:** 7
    **Explanation:** We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].



**Note:**

  1. `1 <= A.length <= 1000`.
  2. `2 <= A[i] <= 10 ^ 9`.


**Tags:** 

**Difficulty:** Medium

**思路:**
