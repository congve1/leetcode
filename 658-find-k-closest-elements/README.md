# 找到 K 个最接近的元素

## 描述

给定一个排序好的数组，两个整数 `k` 和 `x`，从数组中找到最靠近 `x`（两数之差最小）的 `k` 个数。返回的结果必须要是按升序排好的。如果有两个数与 `x` 的差值一样，优先选择数值较小的那个数。

**示例  1:**

    
    
    **输入:** [1,2,3,4,5], k=4, x=3
    **输出:** [1,2,3,4]
    



**示例 2:**

    
    
    **输入:** [1,2,3,4,5], k=4, x=-1
    **输出:** [1,2,3,4]
    



**说明:**

  1. k 的值为正数，且总是小于给定排序数组的长度。
  2. 数组不为空，且长度不超过 104
  3. 数组里的每个元素与 x 的绝对值不超过 104



**更新(2017/9/19):**  
这个参数 _arr_ 已经被改变为一个 **整数数组** （而不是整数列表）。 ** _  请重新加载代码定义以获取最新更改。_**



# Find K Closest Elements

## Description



Given a sorted array, two integers `k` and `x`, find the `k` closest elements to `x` in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

**Example 1:**  

    
    
    **Input:** [1,2,3,4,5], k=4, x=3
    **Output:** [1,2,3,4]
    

**Example 2:**  

    
    
    **Input:** [1,2,3,4,5], k=4, x=-1
    **Output:** [1,2,3,4]
    

**Note:**  

  1. The value k is positive and will always be smaller than the length of the sorted array.
  2. Length of the given array is positive and will not exceed 104
  3. Absolute value of elements in the array and x will not exceed 104

* * *

**UPDATE (2017/9/19):**  
The _arr_ parameter had been changed to an **array of integers** (instead of a list of integers). **_Please reload the code definition to get the latest changes_**.


**Tags:** Binary Search

**Difficulty:** Medium

**思路:**
