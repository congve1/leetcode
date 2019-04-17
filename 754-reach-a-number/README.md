# 到达终点数字

## 描述

在一根无限长的数轴上，你站在`0`的位置。终点在`target`的位置。

每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。

返回到达终点需要的最小移动次数。

**示例 1:**

    
    
    **输入:** target = 3
    **输出:** 2
    **解释:**
    第一次移动，从 0 到 1 。
    第二次移动，从 1 到 3 。
    

**示例 2:**

    
    
    **输入:** target = 2
    **输出:** 3
    **解释:**
    第一次移动，从 0 到 1 。
    第二次移动，从 1 到 -1 。
    第三次移动，从 -1 到 2 。
    

**注意:**

  * `target`是在`[-10^9, 10^9]`范围中的非零整数。



# Reach a Number

## Description



You are standing at position `0` on an infinite number line. There is a goal at position `target`.

On each move, you can either go left or right. During the _n_ -th move (starting from 1), you take _n_ steps.

Return the minimum number of steps required to reach the destination.

**Example 1:**  

    
    
    **Input:** target = 3
    **Output:** 2
    **Explanation:**
    On the first move we step from 0 to 1.
    On the second step we step from 1 to 3.
    

**Example 2:**  

    
    
    **Input:** target = 2
    **Output:** 3
    **Explanation:**
    On the first move we step from 0 to 1.
    On the second move we step  from 1 to -1.
    On the third move we step from -1 to 2.
    

**Note:**  

* `target` will be a non-zero integer in the range `[-10^9, 10^9]`.


**Tags:** Math

**Difficulty:** Easy

**思路:**
