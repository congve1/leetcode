# 两个数组的交集 II

## 描述

给定两个数组，编写一个函数来计算它们的交集。

**示例 1:**

    
    
    **输入:** nums1 = [1,2,2,1], nums2 = [2,2]
    **输出:** [2,2]
    

**示例 2:**

    
    
    **输入:** nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    **输出:** [4,9]

**说明：**

  * 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
  * 我们可以不考虑输出结果的顺序。

****进阶:****

  * 如果给定的数组已经排好序呢？你将如何优化你的算法？
  * 如果  _nums1  _的大小比  _nums2  _小很多，哪种方法更优？
  * 如果  _nums2  _的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？



# Intersection of Two Arrays II

## Description



Given two arrays, write a function to compute their intersection.

**Example 1:**

    
    
    **Input:** nums1 = [1,2,2,1], nums2 = [2,2]
    **Output:** [2,2]
    

**Example 2:**

    
    
    **Input:** nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    **Output:** [4,9]

**Note:**

  * Each element in the result should appear as many times as it shows in both arrays.
  * The result can be in any order.

**Follow up:**

  * What if the given array is already sorted? How would you optimize your algorithm?
  * What if _nums1_ 's size is small compared to _nums2_ 's size? Which algorithm is better?
  * What if elements of _nums2_ are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


**Tags:** Sort, Hash Table, Two Pointers, Binary Search

**Difficulty:** Easy

**思路:**