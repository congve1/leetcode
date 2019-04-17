# 不同的子序列 II

## 描述

给定一个字符串 `S`，计算 `S` 的不同非空子序列的个数。

因为结果可能很大，所以 **返回答案模** **`10^9 + 7`**.



**示例 1：**

    
    
    **输入：** "abc"
    **输出：** 7
    **解释：** 7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
    

**示例 2：**

    
    
    **输入：** "aba"
    **输出：** 6
    **解释：** 6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
    

**示例 3：**

    
    
    **输入：** "aaa"
    **输出：** 3
    **解释：** 3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。
    





**提示：**

  1. `S` 只包含小写字母。
  2. `1 <= S.length <= 2000`







# Distinct Subsequences II

## Description



Given a string `S`, count the number of distinct, non-empty subsequences of `S` .

Since the result may be large, **return the answer modulo`10^9 + 7`**.



**Example 1:**

    
    
    **Input:** "abc"
    **Output:** 7
    **Explanation** : The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
    

**Example 2:**

    
    
    **Input:** "aba"
    **Output:** 6
    **Explanation** : The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
    

**Example 3:**

    
    
    **Input:** "aaa"
    **Output:** 3
    **Explanation** : The 3 distinct subsequences are "a", "aa" and "aaa".
    





**Note:**

  1. `S` contains only lowercase letters.
  2. `1 <= S.length <= 2000`






**Tags:** Dynamic Programming

**Difficulty:** Hard

**思路:**
