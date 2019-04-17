# 最长湍流子数组

## 描述

当 `A` 的子数组 `A[i], A[i+1], ..., A[j]` 满足下列条件时，我们称其为 _湍流子数组_ ：

  * 若 `i <= k < j`，当 `k` 为奇数时， `A[k] > A[k+1]`，且当 `k` 为偶数时，`A[k] < A[k+1]`；
  * **或** 若 `i <= k < j`，当 `k` 为偶数时，`A[k] > A[k+1]` ，且当 `k` 为奇数时， `A[k] < A[k+1]`。

也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 `A` 的最大湍流子数组的 **长度** 。



**示例 1：**

    
    
    **输入：** [9,4,2,10,7,8,8,1,9]
    **输出：** 5
    **解释：** (A[1] > A[2] < A[3] > A[4] < A[5])
    

**示例 2：**

    
    
    **输入：** [4,8,12,16]
    **输出：** 2
    

**示例 3：**

    
    
    **输入：** [100]
    **输出：** 1
    



**提示：**

  1. `1 <= A.length <= 40000`
  2. `0 <= A[i] <= 10^9`



# Longest Turbulent Subarray

## Description



A subarray `A[i], A[i+1], ..., A[j]` of `A` is said to be _turbulent_ if and only if:

  * For `i <= k < j`, `A[k] > A[k+1]` when `k` is odd, and `A[k] < A[k+1]` when `k` is even;
  * **OR** , for `i <= k < j`, `A[k] > A[k+1]` when `k` is even, and `A[k] < A[k+1]` when `k` is odd.

That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the **length** of a maximum size turbulent subarray of A.



**Example 1:**

    
    
    **Input:** [9,4,2,10,7,8,8,1,9]
    **Output:** 5
    **Explanation:** (A[1] > A[2] < A[3] > A[4] < A[5])
    

**Example 2:**

    
    
    **Input:** [4,8,12,16]
    **Output:** 2
    

**Example 3:**

    
    
    **Input:** [100]
    **Output:** 1
    



**Note:**

  1. `1 <= A.length <= 40000`
  2. `0 <= A[i] <= 10^9`


**Tags:** Array, Dynamic Programming, Sliding Window

**Difficulty:** Medium

**思路:**
