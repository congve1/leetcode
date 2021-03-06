# 三等分

## 描述

给定一个由 `0` 和 `1` 组成的数组 `A`，将数组分成 3 个非空的部分，使得所有这些部分表示相同的二进制值。

如果可以做到，请返回 **任何**  `[i, j]`，其中 `i+1 < j`，这样一来：

  * `A[0], A[1], ..., A[i]` 组成第一部分；
  * `A[i+1], A[i+2], ..., A[j-1]` 作为第二部分；
  * `A[j], A[j+1], ..., A[A.length - 1]` 是第三部分。
  * 这三个部分所表示的二进制值相等。

如果无法做到，就返回 `[-1, -1]`。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，`[1,1,0]` 表示十进制中的 `6`，而不会是 `3`。此外，前导零也是被允许的，所以 `[0,1,1]` 和 `[1,1]` 表示相同的值。



**示例 1：**

    
    
    **输入：** [1,0,1,0,1]
    **输出：** [0,3]
    

**示例 2：**

    
    
    **输出：** [1,1,0,1,1]
    **输出：** [-1,-1]



**提示：**

  1. `3 <= A.length <= 30000`
  2. `A[i] == 0` 或 `A[i] == 1`





# Three Equal Parts

## Description



Given an array `A` of `0`s and `1`s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.

If it is possible, return **any** `[i, j]` with `i+1 < j`, such that:

  * `A[0], A[1], ..., A[i]` is the first part;
  * `A[i+1], A[i+2], ..., A[j-1]` is the second part, and
  * `A[j], A[j+1], ..., A[A.length - 1]` is the third part.
  * All three parts have equal binary value.

If it is not possible, return `[-1, -1]`.

Note that the entire part is used when considering what binary value it represents.  For example, `[1,1,0]` represents `6` in decimal, not `3`.  Also, leading zeros are allowed, so `[0,1,1]` and `[1,1]` represent the same value.



**Example 1:**

    
    
    **Input:** [1,0,1,0,1]
    **Output:** [0,3]
    

**Example 2:**

    
    
    **Input:** [1,1,0,1,1]
    **Output:** [-1,-1]



**Note:**

  1. `3 <= A.length <= 30000`
  2. `A[i] == 0` or `A[i] == 1`




**Tags:** Greedy, Math, Binary Search

**Difficulty:** Hard

**思路:**
