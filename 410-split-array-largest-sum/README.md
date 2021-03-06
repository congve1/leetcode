# 分割数组的最大值

## 描述

给定一个非负整数数组和一个整数  _m_ ，你需要将这个数组分成  _m  _个非空的连续子数组。设计一个算法使得这  _m  _个子数组各自和的最大值最小。

**注意:**  
数组长度  _n  _满足以下条件:

  * 1 ≤ _n_ ≤ 1000
  * 1 ≤ _m_ ≤ min(50, _n_ )

**示例:**

    
    
    输入:
    **nums** = [7,2,5,10,8]
    **m** = 2
    
    输出:
    18
    
    解释:
    一共有四种方法将 **nums** 分割为2个子数组。
    其中最好的方式是将其分为 **[7,2,5]** 和 **[10,8]** ，
    因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
    



# Split Array Largest Sum

## Description



Given an array which consists of non-negative integers and an integer _m_ , you can split the array into _m_ non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these _m_ subarrays.

**Note:**  
If _n_ is the length of array, assume the following constraints are satisfied:

  * 1 ≤ _n_ ≤ 1000
  * 1 ≤ _m_ ≤ min(50, _n_ )

**Examples:**

    
    
    Input:
    **nums** = [7,2,5,10,8]
    **m** = 2
    
    Output:
    18
    
    Explanation:
    There are four ways to split **nums** into two subarrays.
    The best way is to split it into **[7,2,5]** and **[10,8]** ,
    where the largest sum among the two subarrays is only 18.
    


**Tags:** Binary Search, Dynamic Programming

**Difficulty:** Hard

**思路:**
