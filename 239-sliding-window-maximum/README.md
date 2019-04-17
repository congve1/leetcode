# 滑动窗口最大值

## 描述

给定一个数组 _nums_ ，有一个大小为  _k  _的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 _k_ 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

**示例:**

    
    
    **输入:** _nums_ = [1,3,-1,-3,5,3,6,7], 和 _k_ = 3
    **输出:**[3,3,5,5,6,7] 
    **解释:**
      滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

**注意：**

你可以假设 _k_ 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

**进阶：**

你能在线性时间复杂度内解决此题吗？



# Sliding Window Maximum

## Description



Given an array _nums_ , there is a sliding window of size _k_ which is moving from the very left of the array to the very right. You can only see the _k_ numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

**Example:**

    
    
    **Input:** _nums_ = [1,3,-1,-3,5,3,6,7], and _k_ = 3
    **Output:**[3,3,5,5,6,7] 
    **Explanation:**
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       **3**
     1 [3  -1  -3] 5  3  6  7       **3**
     1  3 [-1  -3  5] 3  6  7      **5**
     1  3  -1 [-3  5  3] 6  7       **5**
     1  3  -1  -3 [5  3  6] 7       **6**
     1  3  -1  -3  5 [3  6  7]      **7**
    

**Note:**  
You may assume _k_ is always valid, 1 ≤ k ≤ input array's size for non-empty array.

**Follow up:**  
Could you solve it in linear time?


**Tags:** Heap, Sliding Window

**Difficulty:** Hard

**思路:**
