# 颜色分类

## 描述

给定一个包含红色、白色和蓝色，一共  _n_ 个元素的数组， **[原地](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)** 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

**注意:**  
不能使用代码库中的排序函数来解决这道题。

**示例:**

    
    
    **输入:** [2,0,2,1,1,0]
    **输出:** [0,0,1,1,2,2]

**进阶：**

  * 一个直观的解决方案是使用计数排序的两趟扫描算法。  
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。

  * 你能想出一个仅使用常数空间的一趟扫描算法吗？



# Sort Colors

## Description



Given an array with _n_ objects colored red, white or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm) **so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

**Note:**  You are not suppose to use the library's sort function for this problem.

**Example:**

    
    
    **Input:** [2,0,2,1,1,0]
    **Output:** [0,0,1,1,2,2]

**Follow up:**

  * A rather straight forward solution is a two-pass algorithm using counting sort.  
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

  * Could you come up with a one-pass algorithm using only constant space?


**Tags:** Sort, Array, Two Pointers

**Difficulty:** Medium

**思路:**
