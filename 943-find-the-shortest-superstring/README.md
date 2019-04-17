# 最短超级串

## 描述

给定一个字符串数组 `A`，找到以 `A` 中每个字符串作为子字符串的最短字符串。

我们可以假设 `A` 中没有字符串是 `A` 中另一个字符串的子字符串。



**示例 1：**

    
    
    **输入：** ["alex","loves","leetcode"]
    **输出：** "alexlovesleetcode"
    **解释：** "alex"，"loves"，"leetcode" 的所有排列都会被接受。

**示例 2：**

    
    
    **输入：** ["catg","ctaagt","gcta","ttca","atgcatc"]
    **输出：** "gctaagttcatgcatc"



**提示：**

  1. `1 <= A.length <= 12`
  2. `1 <= A[i].length <= 20`





# Find the Shortest Superstring

## Description



Given an array A of strings, find any smallest string that contains each string in `A` as a substring.

We may assume that no string in `A` is substring of another string in `A`.



**Example 1:**

    
    
    **Input:** ["alex","loves","leetcode"]
    **Output:** "alexlovesleetcode"
    **Explanation:** All permutations of "alex","loves","leetcode" would also be accepted.
    

**Example 2:**

    
    
    **Input:** ["catg","ctaagt","gcta","ttca","atgcatc"]
    **Output:** "gctaagttcatgcatc"



**Note:**

  1. `1 <= A.length <= 12`
  2. `1 <= A[i].length <= 20`




**Tags:** Dynamic Programming

**Difficulty:** Hard

**思路:**
