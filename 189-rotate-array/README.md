# 旋转数组

## 描述

给定一个数组，将数组中的元素向右移动  _k  _个位置，其中  _k  _是非负数。

**示例 1:**

    
    
    **输入:** [1,2,3,4,5,6,7] 和 _k_ = 3
    **输出:** [5,6,7,1,2,3,4]
    **解释:**
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
    

**示例  2:**

    
    
    **输入:** [-1,-100,3,99] 和 _k_ = 2
    **输出:** [3,99,-1,-100]
    **解释:** 
    向右旋转 1 步: [99,-1,-100,3]
    向右旋转 2 步: [3,99,-1,-100]

**说明:**

  * 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
  * 要求使用空间复杂度为 O(1) 的原地算法。



# Rotate Array

## Description



Given an array, rotate the array to the right by _k_ steps, where  _k_  is non-negative.

**Example 1:**

    
    
    **Input:** [1,2,3,4,5,6,7] and _k_ = 3
    **Output:** [5,6,7,1,2,3,4]
    **Explanation:**
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    

**Example 2:**

    
    
    **Input:** [-1,-100,3,99] and _k_ = 2
    **Output:** [3,99,-1,-100]
    **Explanation:** 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
    

**Note:**

  * Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
  * Could you do it in-place with O(1) extra space?


**Tags:** Array

**Difficulty:** Easy

**思路:**
