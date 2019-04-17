# 和相同的二元子数组

## 描述

在由若干 `0` 和 `1`  组成的数组 `A` 中，有多少个和为 `S` 的 **非空** 子数组。



**示例：**

    
    
    **输入：** A = [1,0,1,0,1], S = 2
    **输出：** 4
    **解释：**
    如下面黑体所示，有 4 个满足题目要求的子数组：
    [ **1,0,1** ,0,1]
    [ **1,0,1,0** ,1]
    [1, **0,1,0,1** ]
    [1,0, **1,0,1** ]
    



**提示：**

  1. `A.length <= 30000`
  2. `0 <= S <= A.length`
  3. `A[i]` 为 `0` 或 `1`



# Binary Subarrays With Sum

## Description



In an array `A` of `0`s and `1`s, how many **non-empty** subarrays have sum `S`?



**Example 1:**

    
    
    **Input:** A = [1,0,1,0,1], S = 2
    **Output:** 4
    **Explanation:**
    The 4 subarrays are bolded below:
    [ **1,0,1** ,0,1]
    [ **1,0,1,0** ,1]
    [1, **0,1,0,1** ]
    [1,0, **1,0,1** ]
    



**Note:**

  1. `A.length <= 30000`
  2. `0 <= S <= A.length`
  3. `A[i]` is either `0` or `1`.


**Tags:** Hash Table, Two Pointers

**Difficulty:** Medium

**思路:**
