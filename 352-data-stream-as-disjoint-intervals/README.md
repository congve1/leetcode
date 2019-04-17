# 将数据流变为多个不相交区间

## 描述

给定一个非负整数的数据流输入 a1，a2，…，an，…，将到目前为止看到的数字总结为不相交的区间列表。

例如，假设数据流中的整数为 1，3，7，2，6，…，每次的总结为：

    
    
    [1, 1]
    [1, 1], [3, 3]
    [1, 1], [3, 3], [7, 7]
    [1, 3], [7, 7]
    [1, 3], [6, 7]
    



**进阶：**  
如果有很多合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?

**提示：**  
特别感谢 [@yunhong](https://discuss.leetcode.com/user/yunhong) 提供了本问题和其测试用例。



# Data Stream as Disjoint Intervals

## Description



Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

    
    
    [1, 1]
    [1, 1], [3, 3]
    [1, 1], [3, 3], [7, 7]
    [1, 3], [7, 7]
    [1, 3], [6, 7]
    

**Follow up:**  
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?


**Tags:** Binary Search Tree

**Difficulty:** Hard

**思路:**
