# 最佳观光组合

## 描述

给定正整数数组 `A`，`A[i]` 表示第 `i` 个观光景点的评分，并且两个景点 `i` 和 `j` 之间的距离为 `j - i`。

一对景点（`i < j`）组成的观光组合的得分为（`A[i] + A[j] + i - j`）：景点的评分之和 **减去** 它们两者之间的距离。

返回一对观光景点能取得的最高分。



**示例：**

    
    
    **输入：** [8,1,5,2,6]
    **输出：** 11
    **解释：** i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
    



**提示：**

  1. `2 <= A.length <= 50000`
  2. `1 <= A[i] <= 1000`



# Best Sightseeing Pair

## Description



Given an array `A` of positive integers, `A[i]` represents the value of the `i`-th sightseeing spot, and two sightseeing spots `i` and `j` have distance `j - i` between them.

The _score_  of a pair (`i < j`) of sightseeing spots is (`A[i] + A[j] + i - j)` : the sum of the values of the sightseeing spots, **minus** the distance between them.

Return the maximum score of a pair of sightseeing spots.



**Example 1:**

    
    
    **Input:** [8,1,5,2,6]
    **Output:** 11
    **Explanation:** i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
    



**Note:**

  1. `2 <= A.length <= 50000`
  2. `1 <= A[i] <= 1000`


**Tags:** Array

**Difficulty:** Medium

**思路:**
