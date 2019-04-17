# 子数组的最小值之和

## 描述

给定一个整数数组 `A`，找到 `min(B)` 的总和，其中 `B` 的范围为 `A` 的每个（连续）子数组。

由于答案可能很大，因此 **返回答案模`10^9 + 7`**。



**示例：**

    
    
    **输入：** [3,1,2,4]
    **输出：** 17
    **解释：
    子数组为** [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
    最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。



**提示：**

  1. `1 <= A <= 30000`
  2. `1 <= A[i] <= 30000`





# Sum of Subarray Minimums

## Description



Given an array of integers `A`, find the sum of `min(B)`, where `B` ranges over every (contiguous) subarray of `A`.

Since the answer may be large, **return the answer modulo`10^9 + 7`.**



**Example 1:**

    
    
    **Input:** [3,1,2,4]
    **Output:** 17
    **Explanation:** Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
    Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.



**Note:**

  1. `1 <= A.length <= 30000`
  2. `1 <= A[i] <= 30000`




**Tags:** Stack, Array

**Difficulty:** Medium

**思路:**
