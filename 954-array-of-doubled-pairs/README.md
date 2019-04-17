# 二倍数对数组

## 描述

给定一个长度为偶数的整数数组 `A`，只有对 `A` 进行重组后可以满足 "对于每个 `0 <= i < len(A) / 2`，都有 `A[2 * i + 1] = 2 * A[2 * i]`" 时，返回 `true`；否则，返回 `false`。



**示例 1：**

    
    
    **输入：** [3,1,3,6]
    **输出：** false
    

**示例 2：**

    
    
    **输入：** [2,1,2,6]
    **输出：** false
    

**示例 3：**

    
    
    **输入：** [4,-2,2,-4]
    **输出：** true
    **解释：** 我们可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]

**示例 4：**

    
    
    **输入：** [1,2,4,16,8,4]
    **输出：** false
    



**提示：**

  1. `0 <= A.length <= 30000`
  2. `A.length` 为偶数
  3. `-100000 <= A[i] <= 100000`



# Array of Doubled Pairs

## Description



Given an array of integers `A` with even length, return `true` if and only if it is possible to reorder it such that `A[2 * i + 1] = 2 * A[2 * i]` for every `0 <= i < len(A) / 2`.



**Example 1:**

    
    
    **Input:** [3,1,3,6]
    **Output:** false
    

**Example 2:**

    
    
    **Input:** [2,1,2,6]
    **Output:** false
    

**Example 3:**

    
    
    **Input:** [4,-2,2,-4]
    **Output:** true
    **Explanation:** We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
    

**Example 4:**

    
    
    **Input:** [1,2,4,16,8,4]
    **Output:** false
    



**Note:**

  1. `0 <= A.length <= 30000`
  2. `A.length` is even
  3. `-100000 <= A[i] <= 100000`


**Tags:** Array, Hash Table

**Difficulty:** Medium

**思路:**
