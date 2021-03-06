# 优美的排列

## 描述

假设有从 1 到 N 的  **N  **个整数，如果从这  **N  **个数字中成功构造出一个数组，使得数组的第 **i**  位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

  1. 第  **i  **位的数字能被  **i  **整除
  2. **i** 能被第 **i** 位上的数字整除

现在给定一个整数 N，请问可以构造多少个优美的排列？

**示例1:**

    
    
    **输入:** 2
    **输出:** 2
    **解释:** 
    
    第 1 个优美的排列是 [1, 2]:
      第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
      第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除
    
    第 2 个优美的排列是 [2, 1]:
      第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
      第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
    

**说明:**

  1. **N** 是一个正整数，并且不会超过15。



# Beautiful Arrangement

## Description



Suppose you have **N** integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these **N** numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

  1. The number at the ith position is divisible by **i**.
  2. **i** is divisible by the number at the ith position.



Now given N, how many beautiful arrangements can you construct?

**Example 1:**

    
    
    **Input:** 2
    **Output:** 2
    **Explanation:** 
    
    The first beautiful arrangement is [1, 2]:
    
    Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
    
    Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
    
    The second beautiful arrangement is [2, 1]:
    
    Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
    
    Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
    



**Note:**

  1. **N** is a positive integer and will not exceed 15.




**Tags:** Backtracking

**Difficulty:** Medium

**思路:**
