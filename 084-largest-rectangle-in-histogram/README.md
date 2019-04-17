# 柱状图中最大的矩形

## 描述

给定 _n_ 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。



![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram.png)

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 `[2,1,5,6,2,3]`。



![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram_area.png)

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 `10` 个单位。



**示例:**

    
    
    **输入:** [2,1,5,6,2,3]
    **输出:** 10



# Largest Rectangle in Histogram

## Description



Given _n_ non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.



![](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)  
Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.



![](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)  
The largest rectangle is shown in the shaded area, which has area = `10` unit.



**Example:**

    
    
    **Input:** [2,1,5,6,2,3]
    **Output:** 10
    


**Tags:** Stack, Array

**Difficulty:** Hard

**思路:**
