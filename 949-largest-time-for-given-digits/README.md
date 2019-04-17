# 给定数字能组成的最大时间

## 描述

给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。

最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。

以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。



**示例 1：**

    
    
    **输入：** [1,2,3,4]
    **输出：** "23:41"
    

**示例 2：**

    
    
    **输入：** [5,5,5,5]
    **输出：** ""
    



**提示：**

  1. `A.length == 4`
  2. `0 <= A[i] <= 9`



# Largest Time for Given Digits

## Description



Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



**Example 1:**

    
    
    **Input:** [1,2,3,4]
    **Output:** "23:41"
    

**Example 2:**

    
    
    **Input:** [5,5,5,5]
    **Output:** ""
    



**Note:**

  1. `A.length == 4`
  2. `0 <= A[i] <= 9`


**Tags:** Math

**Difficulty:** Easy

**思路:**
