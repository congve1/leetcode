# 插入区间

## 描述

给出一个 _无重叠的 ，_ 按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

**示例  1:**

    
    
    **输入:** intervals = [[1,3],[6,9]], newInterval = [2,5]
    **输出:** [[1,5],[6,9]]
    

**示例  2:**

    
    
    **输入:** intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    **输出:** [[1,2],[3,10],[12,16]]
    **解释:** 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
    



# Insert Interval

## Description



Given a set of _non-overlapping_ intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

**Example 1:**

    
    
    **Input:** intervals = [[1,3],[6,9]], newInterval = [2,5]
    **Output:** [[1,5],[6,9]]
    

**Example 2:**

    
    
    **Input:** intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    **Output:** [[1,2],[3,10],[12,16]]
    **Explanation:** Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


**Tags:** Sort, Array

**Difficulty:** Hard

**思路:**
