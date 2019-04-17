# 计算右侧小于当前元素的个数

## 描述

给定一个整数数组 _nums_ ，按要求返回一个新数组  _counts_ 。数组 _counts_ 有该性质： `counts[i]` 的值是  `nums[i]` 右侧小于 `nums[i]` 的元素的数量。

**示例:**

    
    
    **输入:** [5,2,6,1]
    **输出:** [2,1,1,0] 
    **解释:**
    5 的右侧有 **2** 个更小的元素 (2 和 1).
    2 的右侧仅有 **1** 个更小的元素 (1).
    6 的右侧有 **1** 个更小的元素 (1).
    1 的右侧有 **0** 个更小的元素.
    



# Count of Smaller Numbers After Self

## Description



You are given an integer array _nums_ and you have to return a new _counts_ array. The _counts_ array has the property where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

**Example:**

    
    
    **Input:** [5,2,6,1]
    **Output:** [2,1,1,0] 
    **Explanation:**
    To the right of 5 there are **2** smaller elements (2 and 1).
    To the right of 2 there is only **1** smaller element (1).
    To the right of 6 there is **1** smaller element (1).
    To the right of 1 there is **0** smaller element.
    


**Tags:** Binary Indexed Tree, Segment Tree, Binary Search Tree, Divide and Conquer

**Difficulty:** Hard

**思路:**
