# 连续差相同的数字

## 描述

返回所有长度为 `N` 且满足其每两个连续位上的数字之间的差的绝对值为 `K` 的 **非负整数** 。

请注意， **除了** 数字 `0` 本身之外，答案中的每个数字都 **不能** 有前导零。例如，`01` 因为有一个前导零，所以是无效的；但 `0` 是有效的。

你可以按任何顺序返回答案。



**示例 1：**

    
    
    **输入：** N = 3, K = 7
    **输出：** [181,292,707,818,929]
    **解释：** 注意，070 不是一个有效的数字，因为它有前导零。
    

**示例 2：**

    
    
    **输入：** N = 2, K = 1
    **输出：** [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]



**提示：**

  1. `1 <= N <= 9`
  2. `0 <= K <= 9`



# Numbers With Same Consecutive Differences

## Description



Return all **non-negative** integers of length `N` such that the absolute difference between every two consecutive digits is `K`.

Note that **every** number in the answer **must not** have leading zeros **except** for the number `0` itself. For example, `01` has one leading zero and is invalid, but `0` is valid.

You may return the answer in any order.



**Example 1:**

    
    
    **Input:** N = 3, K = 7
    **Output:** [181,292,707,818,929]
    **Explanation:** Note that 070 is not a valid number, because it has leading zeroes.
    

**Example 2:**

    
    
    **Input:** N = 2, K = 1
    **Output:** [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]



**Note:**

  1. `1 <= N <= 9`
  2. `0 <= K <= 9`


**Tags:** Dynamic Programming

**Difficulty:** Medium

**思路:**
