# 翻转对

## 描述

给定一个数组 `nums` ，如果 `i < j` 且 `nums[i] > 2*nums[j]` 我们就将 `(i, j)` 称作一个 ** _重要翻转对_** 。

你需要返回给定数组中的重要翻转对的数量。

**示例 1:**

    
    
    **输入** : [1,3,2,3,1]
    **输出** : 2
    

**示例 2:**

    
    
    **输入** : [2,4,3,5,1]
    **输出** : 3
    

**注意:**

  1. 给定数组的长度不会超过`50000`。
  2. 输入数组中的所有数字都在32位整数的表示范围内。



# Reverse Pairs

## Description



Given an array `nums`, we call `(i, j)` an **_important reverse pair_** if `i < j` and `nums[i] > 2*nums[j]`.

You need to return the number of important reverse pairs in the given array.

**Example1:**

    
    
    **Input** : [1,3,2,3,1]
    **Output** : 2
    

**Example2:**

    
    
    **Input** : [2,4,3,5,1]
    **Output** : 3
    

**Note:**  

  1. The length of the given array will not exceed `50,000`.
  2. All the numbers in the input array are in the range of 32-bit integer.


**Tags:** Binary Indexed Tree, Segment Tree, Binary Search Tree, Divide and Conquer

**Difficulty:** Hard

**思路:**
